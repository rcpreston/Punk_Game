debug = true

bump = require 'bump'
JSON = require 'json'
anim8 = require 'anim8'
gamera = require 'gamera'
shakycam = require 'shakycam'


-- Player/Scene containers
Character = nil
Scene = nil
Player = nil
Map = {0,0}
current_map = 1

-- Collision stuff
world = bump.newWorld()

-- Camera stuff
cam = gamera.new(0,0,2000,2000)
cam:setWindow(0,0,640,480)

-- Image Storage

-- Map Item Storage

-- Enemy Storage
enemies = {} -- array of current enemies on screen

-- NPC Storage
npcs = {}

function love.load(arg)
	choice = 2
	timer = 0.2
	-- What to draw list
	isCharSelect = true -- Are we on the character screen?
	isSceneSelect = false -- Are we on the scene selection screen?
	isPlayScene = false -- Are we playing the fucking game?
	isShowMenu = false -- Are we derping in the menu?

	def_r,def_b,def_g = love.graphics.getColor()

	-- Trying animation with anim8
	image = love.graphics.newImage('assets/Character/bunsheet.png')
  	local g = anim8.newGrid(30, 47, image:getWidth(), image:getHeight())
  	player = {
  		walk_timer = 0.05,
  		run_timer = 0.000005,
  		y_pos = 200,
  		x_pos = 305,
  		direction = "D",
  		stop = true,
  		down = anim8.newAnimation(g('1-4',1), 0.2),
  		down_s = anim8.newAnimation(g(2,1), 0.2),
  		up = anim8.newAnimation(g('1-4',3), 0.2),
  		up_s = anim8.newAnimation(g(2,3), 0.2),
  		left_w = anim8.newAnimation(g('1-4',2), 0.2),
  		left_s = anim8.newAnimation(g(2,2), 0.2),
  		left_r = anim8.newAnimation(g('1-6',4), 0.1),
  		right_w = anim8.newAnimation(g('1-4',2), 0.2):flipH(),
  		right_s = anim8.newAnimation(g(2,2), 0.2):flipH(),
  		right_r = anim8.newAnimation(g('1-6',4), 0.1):flipH()
  	}

  	-- Menu creation
  	local a= love.filesystem.read("assets/Menu/options.js")
	options = JSON:decode(a)
	background = love.graphics.newImage("assets/Menu/background.png")
	menuback = love.graphics.newImage("assets/Menu/backarrow.png")
	phone = {
		timer = 0.2,
		choice = 0,
		left= 188,
		right = 462,
		top = 18,
		bottom = 452,
		midpoint = 188+ 274/2,
		height = 434,
		width = 274
	}
	menu = "main"
	sub = 0

	-- Fonts!
	titleFont = love.graphics.newFont("assets/Font/MARSNEVENEKSK.otf",60)
	subFont = love.graphics.newFont("assets/Font/PaintCans.ttc",20)
	speechFont = love.graphics.newFont("assets/Font/PaintCans.ttc",12)
	numberFont = love.graphics.newFont("assets/Font/PaintCans.ttc",14)
	menuFont = love.graphics.newFont("assets/Font/nokiafc22.ttf",24)
	runningTime = 0
	-- Character json
	a = love.filesystem.read("assets/Character/char_list.js")
	char_list = JSON:decode(a)
end

function love.update(dt)
	-- GTFO from the game
	if love.keyboard.isDown('escape') then
		love.event.push('quit')
	end
	runningTime = runningTime + dt
	
	if isCharSelect then
		charselectUpdate(dt)
	elseif isSceneSelect then
	    sceneselectUpdate(dt)
	elseif isPlayScene then
		gameUpdate(dt)
	end

end

function love.draw(dt)
	love.graphics.print("Total Running Time: "..runningTime.."s",10,400)
	love.graphics.print("FPS: "..love.timer.getFPS(),10,440)
	if isCharSelect then
		charselectDraw()
	elseif isSceneSelect then
	    sceneselectDraw()
	elseif isPlayScene then
	    gameDraw()
	end
	

end

function charselectDraw()
	-- Draw the current character select menu
	love.graphics.setFont(titleFont)
	text = "< Choose Your Player >"
	love.graphics.print(text,320-titleFont:getWidth(text)/2,5)
	love.graphics.setFont(subFont)
	text = char_list[choice].name
	
	love.graphics.print(text,480-subFont:getWidth(text)/2,80)
	local mug = love.graphics.newImage('assets/Character/'..char_list[choice].face)
	love.graphics.draw(mug,10,30)
	love.graphics.setFont(speechFont)
	local height =subFont:getHeight("L")+90
	text = "Age "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = tostring(char_list[choice].age)
	love.graphics.print(text,600-numberFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	love.graphics.setFont(speechFont)
	text = "Gender "
	love.graphics.print(text,400,height)
	text = char_list[choice].gender
	love.graphics.print(text,600-speechFont:getWidth(text),height)

	height = height + speechFont:getHeight("A") + 5
	text = "HP "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = char_list[choice].hp_base
	love.graphics.print(text,600-numberFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	love.graphics.setFont(speechFont)
	text = "Attack "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = char_list[choice].atk_base
	love.graphics.print(text,600-numberFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	love.graphics.setFont(speechFont)
	text = "Defense "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = char_list[choice].def_base
	love.graphics.print(text,600-numberFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	love.graphics.setFont(speechFont)
	text = "Speed "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = char_list[choice].spd_base
	love.graphics.print(text,600-numberFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	love.graphics.setFont(speechFont)
	text = "Stamina "
	love.graphics.print(text,400,height)
	love.graphics.setFont(numberFont)
	text = char_list[choice].sta_base
	love.graphics.print(text,600-numberFont:getWidth(text),height)

end

function charselectUpdate(dt)
	-- Updating what character is selected
	timer = timer - dt

	if love.keyboard.isDown('escape') then
		love.event.push('quit')
	end

	if love.keyboard.isDown('left','a') and timer <= 0 then
		if choice == 2 then -- swap to last char in list
			choice = tonumber(char_list[1].char_num)+1
		else
		    choice =choice -1
		end
		image = love.graphics.newImage('assets/Character/'..char_list[choice].model..'.png')
		timer = 0.2
	elseif love.keyboard.isDown('right','d') and timer <= 0 then
		if choice == tonumber(char_list[1].char_num)+1 then -- swap to first char in list
			choice = 2
		else
		    choice = choice +1
		end
		image = love.graphics.newImage('assets/Character/'..char_list[choice].model..'.png')
		timer = 0.2
	elseif love.keyboard.isDown('return') and timer <= 0 then
		isCharSelect = false
		isSceneSelect = true
		Character = char_list[choice]
		image = love.graphics.newImage('assets/Character/'..char_list[choice].model..'.png')
		choice = 2
		timer = 0.2
	end


end

function sceneselectDraw()
	-- Draw our scene selection page
	love.graphics.setFont(titleFont)
	text = "Scene Selection"
	love.graphics.print(text,320-titleFont:getWidth(text)/2,5)

	local height = 100
	local x_dist = 170
	local line = love.graphics.newImage("assets/Character/"..Character.select_line..".png")
	love.graphics.draw(line, x_dist-30+20*(choice-2),height+40*(choice-2))

	love.graphics.setFont(subFont)
	print(tostring(Character.scenelist[1].scene_num))
	for i=2,1+Character.scenelist[1].scene_num do
		text = Character.scenelist[i].Title
		love.graphics.print(text,x_dist,height)
		height = height + 40
		x_dist = x_dist + 20
	end

end

function sceneselectUpdate(dt)
	-- Update what scene is selected
	timer = timer - dt

	if love.keyboard.isDown('escape') then
		love.event.push('quit')
	end

	if love.keyboard.isDown('up','w') and timer <= 0 then
		if choice == 2 then -- swap to last char in list
			choice = tonumber(Character.scenelist[1].scene_num)+1
		else
		    choice = choice-1
		end
		timer = 0.2
	elseif love.keyboard.isDown('down','s') and timer <= 0 then
		if choice == tonumber(Character.scenelist[1].scene_num)+1 then -- swap to first char in list
			choice = 2
		else
		    choice = choice+ 1
		end
		timer = 0.2
	end

	if love.keyboard.isDown('return') and timer <= 0 then
		isSceneSelect = false
		isPlayScene = true
		Scene = Character.scenelist[choice].File
		mapLoad()
		choice = 2
		timer = 0.2
	end
end

function playerUpdate(dt)
	player.walk_timer = player.walk_timer - dt
	player.run_timer = player.run_timer - dt

	if love.keyboard.isDown('down','s') then
		player.down:update(dt)
		if player.walk_timer <= 0 and player.y_pos < 437 then
			player.y_pos = player.y_pos + 1
			player.walk_timer = 0.05
		end
		player.direction = "D"
		player.stop = false
	elseif love.keyboard.isDown('up','w') then
		player.up:update(dt)
		if player.walk_timer <= 0 and player.y_pos > 0 then
			player.y_pos = player.y_pos - 1
			player.walk_timer = 0.05
		end
		world:move(player,player.x_pos,player.y_pos)
		player.direction = "U"
		player.stop = false
	elseif love.keyboard.isDown('left','a') then
		player.left_r:update(dt)
		player.direction = "L"
		player.stop = false
	elseif love.keyboard.isDown('right','d') then
		player.right_r:update(dt)
		player.direction = "R"
		player.stop = false
	else
		player.stop = true
	end
	player.x_pos,player.y_pos = world:move(player,player.x_pos,player.y_pos)

end

function playerDraw()
	if player.direction == "D" then
		if not player.stop then
			player.down:draw(image,player.x_pos,player.y_pos)
		else
		    player.down_s:draw(image,player.x_pos,player.y_pos)
		end
	elseif player.direction == "U" then
	    if not player.stop then
	        player.up:draw(image,player.x_pos,player.y_pos)
	    else
	        player.up_s:draw(image,player.x_pos,player.y_pos)
	    end
	elseif player.direction == "L" then
	    if not player.stop then
	        player.left_r:draw(image,player.x_pos,player.y_pos)
	    else
	        player.left_s:draw(image,player.x_pos,player.y_pos)
	    end
	elseif player.direction == "R" then
	    if not player.stop then
	        player.right_r:draw(image,player.x_pos,player.y_pos)
	    else
	        player.right_s:draw(image,player.x_pos,player.y_pos)
	    end
	end
end		

function gameUpdate(dt)
	if love.keyboard.isDown('escape') then
		love.event.push('quit')
	end

	if love.keyboard.isDown('m') then
		isShowMenu = true
	end
	
	if isShowMenu then
		menuUpdate(dt)
	else
		playerUpdate(dt)
		mapUpdate(dt)
	end
end

function gameDraw(dt)
	if isShowMenu then
		menuDraw()
	else
		mapDraw()
	end
end

function menuDraw()
	love.graphics.draw(background,0,0)
	love.graphics.setFont(menuFont)
	love.graphics.setLineWidth(4)
	love.graphics.setColor(20,20,175)
	if menu == "main" then
		if phone.choice == tonumber(options[1].num) then			
			love.graphics.rectangle("fill",phone.left,phone.bottom-menuback:getHeight()-8,phone.width,menuback:getHeight()+9)
		else
		    love.graphics.rectangle("fill",phone.left,phone.top+38*(phone.choice),phone.width,34)
		end
		local y = phone.top+2
		for i=2,1+tonumber(options[1].num) do
			love.graphics.setColor(185,185,185)
			text = options[i].name
			love.graphics.print(text,phone.midpoint-menuFont:getWidth(text)/2,y)
			y = y + 34
			love.graphics.setColor(0,0,0)
			love.graphics.line(phone.left,y,phone.right,y)
			y = y + 4
		end
	elseif menu == "sub" then
		if phone.choice == tonumber(options[sub].list[1].num) then
			love.graphics.rectangle("fill",phone.left,phone.bottom-menuback:getHeight()-8,phone.width,menuback:getHeight()+9)
		else
		    love.graphics.rectangle("fill",phone.left,phone.top+38*(phone.choice),phone.width,34)
		end
		local y = phone.top+2
		for i=2,1+tonumber(options[sub].list[1].num) do
			love.graphics.setColor(185,185,185)
			text = options[sub].list[i].name
			love.graphics.print(text,phone.midpoint-menuFont:getWidth(text)/2,y)
			y = y + 34
			love.graphics.setColor(0,0,0)
			love.graphics.line(phone.left,y,phone.right,y)
			y = y + 4
		end
	end
	love.graphics.setColor(def_r,def_b,def_g)
	love.graphics.draw(menuback,phone.midpoint-menuback:getWidth()/2,phone.bottom-menuback:getHeight()-4)
end

function menuUpdate(dt)
	phone.timer = phone.timer - dt
	if love.keyboard.isDown('up','w') and phone.timer <= 0 then
		if phone.choice == 0 then
			if menu == "main" then
				phone.choice = tonumber(options[1].num)
			elseif menu == "sub" then
				phone.choice = tonumber(options[sub].list[1].num)
			end
		else
		    phone.choice = phone.choice - 1
		end
		phone.timer = 0.2
	elseif love.keyboard.isDown('down','s') and phone.timer <= 0 then
	    
		if menu == "main" then
			if phone.choice == tonumber(options[1].num) then
				phone.choice = 0
			else
			    phone.choice = phone.choice + 1
			end
		elseif menu == "sub" then
			if phone.choice == tonumber(options[sub].list[1].num) then
				phone.choice = 0
			else
			    phone.choice = phone.choice + 1
			end
		end
		phone.timer = 0.2
	elseif love.keyboard.isDown('return') and phone.timer <= 0 then
	    if menu == "main" then
	    	if phone.choice == tonumber(options[1].num) then
	    		isShowMenu = false
	    		phone.choice = 0
	    	else
	    		menu = "sub"
	    		sub = phone.choice+2
	    		phone.choice = 0
	    	end
	    elseif menu == "sub" then
	    	if phone.choice == tonumber(options[sub].list[1].num) then
	    		menu = "main"
	    		sub = 0
	    		phone.choice = 0
	    	else
	    		--do specific things with functions and junk
	    	end
	    end
	    phone.timer = 0.2
	end
end

function mapUpdate(dt)
	if checkColl() == true then
	-- Move map
		mapMove()
	-- First check if player location is on map portal location
	-- Then check if player triggered event
	end
end

function mapDraw()
	love.graphics.draw(background,0,0)
	love.graphics.draw(Map[current_map].bg,Map[current_map].bg_x,0)
	for i=2, Map[current_map].back_list[1]+1 do
		love.graphics.draw(Map[current_map].back_list[i].image,Map[current_map].back_list[i].x,0)
	end
	love.graphics.draw(Map[current_map].floor,Map[current_map].floor_x,0)
	playerDraw()
	love.graphics.draw(Map[current_map].front,Map[current_map].front_x,0)
end

function mapLoad()
	local a = love.filesystem.read("assets/Scene/"..Scene.."/map_info.js")
	map_info = JSON:decode(a)

	for i=2,tonumber(map_info[1].num)+1 do
		local a = love.filesystem.read("assets/Map/"..map_info[i].folder.."/walls.js")
		local wall_list = JSON:decode(a)
		a = love.filesystem.read("assets/Map/"..map_info[i].folder.."/portals.js")
		local portal_list = JSON:decode(a)
		back_list = {0,0}
		back_list[1] = tonumber(map_info[i].back_item[1].num)
		for j=2,back_list[1]+1 do
			back_list[j] = {
				image = love.graphics.newImage(map_info[i].back_item[j].image),
				speed = tonumber(map_info[i].back_item[j].speed),
				x = 0
			}
		end
		portals = {}
		portals[1] = tonumber(portal_list[1].num)
		for j=2,portals[1]+1 do
			portals[j] = {
				name = portal_list[j].name,
				dest_map = portal_list[j].folder,
				portal_x = tonumber(portal_list[j].portal_x),
				portal_y = tonumber(portal_list[j].portal_y),
				width = tonumber(portal_list[j].portal_width),
				height = tonumber(portal_list[j].portal_height),
				dest_x = tonumber(portal_list[j].dest_x),
				dest_y = tonumber(portal_list[j].dest_y)
			}
		end
		walls = {}
		walls[1] = tonumber(wall_list[1].num)
		for j=2,walls[1]+1 do
			walls[j] = {
				x = tonumber(wall_list[j].x_loc),
				y = tonumber(wall_list[j].y_loc),
				width = tonumber(wall_list[j].width),
				height = tonumber(wall_list[j].height)
			}
		end
		Map[i-1] = {
			bg = love.graphics.newImage(map_info[i].bg),
			bg_x = 0,
			floor = love.graphics.newImage(map_info[i].floor),
			floor_spd = tonumber(map_info[i].floor_speed),
			floor_x = 0,
			front = love.graphics.newImage(map_info[i].front),
			front_spd = tonumber(map_info[i].front_speed),
			front_x = 0,
			walls = walls,
			back_list = back_list,
			object_list = map_info[i].objects,
			npc_list = map_info[i].npcs,
			portals = portals,
	}
	end
	changeWorld()
end

function changeWorld()
	world = bump.newWorld()
	world:add(player,player.x_pos,player.y_pos,30,47)
	for i=2,Map[current_map].walls[1]+1 do
		world:add(Map[current_map].walls[i],Map[current_map].walls[i].x,Map[current_map].walls[i].y,Map[current_map].walls[i].width,Map[current_map].walls[i].height)
	end
end

function mapMove()
	if player.direction == "L" and not player.stop then
		-- Update images
		for i=2,Map[current_map].back_list[1]+1 do
			Map[current_map].back_list[i].x = Map[current_map].back_list[i].x + Map[current_map].back_list[i].speed
		end
		Map[current_map].floor_x = Map[current_map].floor_x + Map[current_map].floor_spd
		Map[current_map].front_x = Map[current_map].front_x + Map[current_map].front_spd
		-- Update walls
		for i=2,Map[current_map].walls[1]+1 do
			Map[current_map].walls[i].x = Map[current_map].walls[i].x + Map[current_map].floor_spd
			world:move(Map[current_map].walls[i],Map[current_map].walls[i].x,Map[current_map].walls[i].y)
		end
		-- Update objects
		-- Update NPCS
	elseif player.direction == "R" and not player.stop then
		-- Update images
	    for i=2,Map[current_map].back_list[1]+1 do
			Map[current_map].back_list[i].x = Map[current_map].back_list[i].x - Map[current_map].back_list[i].speed
		end
		Map[current_map].floor_x = Map[current_map].floor_x - Map[current_map].floor_spd
		Map[current_map].front_x = Map[current_map].front_x - Map[current_map].front_spd
		-- Update walls
		for i=2,Map[current_map].walls[1]+1 do
			Map[current_map].walls[i].x = Map[current_map].walls[i].x - Map[current_map].floor_spd
			world:move(Map[current_map].walls[i],Map[current_map].walls[i].x,Map[current_map].walls[i].y)
		end
		-- Update objects
		-- Update NPCS
	end
end

function checkColl()
	local move = true
	local speed = Map[current_map].floor_spd
	if player.direction == "L" and not player.stop then
		for i=2,Map[current_map].walls[1]+1 do
			local x = world:check(Map[current_map].walls[i],Map[current_map].walls[i].x+ speed,Map[current_map].walls[i].y)
			if x ~= Map[current_map].walls[i].x + speed then
				move = false
			end
		end
	elseif player.direction == "R" and not player.stop then
		for i=2,Map[current_map].walls[1]+1 do
			local x = world:check(Map[current_map].walls[i],Map[current_map].walls[i].x- speed,Map[current_map].walls[i].y)
			if x ~= Map[current_map].walls[i].x - speed then
				move = false
			end
		end
	end
	return move
end

-- if love.keyboard.isDown('left','a') then
-- 		if player.x > 0 then -- binds us to the map
-- 			player.x = player.x - (player.speed*dt)
-- 		end
-- 	elseif love.keyboard.isDown('right','d') then
-- 		if player.x < (love.graphics.getWidth()-player.img:getWidth()) then
-- 			player.x = player.x + (player.speed*dt)
-- 		end
-- 	end