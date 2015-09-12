debug = true

bump = require 'bump'
JSON =require 'json'

choice = 2
timer = 0.2
-- What to draw list
isCharSelect = true -- Are we on the character screen?
isSceneSelect = false -- Are we on the scene selection screen?
isPlayScene = false -- Are we playing the fucking game?
isShowMenu = false -- Are we derping in the menu?

-- Character json
a= love.filesystem.read("assets/Character/char_list.js")
print(a)
char_list = JSON:decode(a)
print(char_list)
--char_list = json.decode(love.filesystem.read("assets/Character/char_list.js"))

-- Player/Scene containers
Character = nil
Scene = nil
Player = nil

-- Fonts!
titleFont = love.graphics.newFont("assets/Font/MARSNEVENEKSK.otf",60)
subFont = love.graphics.newFont("assets/Font/PaintCans_09_FREE.otf",20)
speechFont = love.graphics.newFont("assets/Font/PaintCans_09_FREE.otf",12)
menuFont = love.graphics.newFont("assets/Font/nokiafc22.ttf",24)

-- Image Storage

-- Map Item Storage

-- Enemy Storage
enemies = {} -- array of current enemies on screen

-- NPC Storage
npcs = {}

function love.load(arg)
	--player.img = love.graphics.newImage('res/Character/Char1/spritesheet.png')
	-- And now we got a pretty little spritesheet
end

function love.update(dt)
	-- GTFO from the game
	if love.keyboard.isDown('escape') then
		love.event.push('quit')
	end

	if isCharSelect then
		charselectUpdate(dt)
	elseif isSceneSelect then
	    sceneselectUpdate(dt)
	end

end

function love.draw(dt)
	if isCharSelect then
		charselectDraw()
	elseif isSceneSelect then
	    sceneselectDraw()
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

	love.graphics.setFont(speechFont)
	local height =subFont:getHeight("L")+90
	text = "Age - "
	love.graphics.print(text,400,height)
	text = tostring(char_list[choice].age)
	love.graphics.print(text,600-speechFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	text = "Gender - "
	love.graphics.print(text,400,height)
	text = char_list[choice].gender
	love.graphics.print(text,600-speechFont:getWidth(text),height)

	height = height + speechFont:getHeight("A") + 5
	text = "HP - "
	love.graphics.print(text,400,height)
	text = char_list[choice].hp_base
	love.graphics.print(text,600-speechFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	text = "Attack - "
	love.graphics.print(text,400,height)
	text = char_list[choice].atk_base
	love.graphics.print(text,600-speechFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	text = "Defense - "
	love.graphics.print(text,400,height)
	text = char_list[choice].def_base
	love.graphics.print(text,600-speechFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	text = "Speed - "
	love.graphics.print(text,400,height)
	text = char_list[choice].spd_base
	love.graphics.print(text,600-speechFont:getWidth(text),height)
	height = height + speechFont:getHeight("A") + 5
	text = "Stamina - "
	love.graphics.print(text,400,height)
	text = char_list[choice].sta_base
	love.graphics.print(text,600-speechFont:getWidth(text),height)

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
		timer = 0.2
	elseif love.keyboard.isDown('right','d') and timer <= 0 then
		if choice == tonumber(char_list[1].char_num)+1 then -- swap to first char in list
			choice = 2
		else
		    choice = choice +1
		end
		timer = 0.2
	elseif love.keyboard.isDown('return') then
		isCharSelect = false
		isSceneSelect = true
		Character = char_list[choice]
		choice = 2
	end

end

function sceneselectDraw()
	-- Draw our scene selection page
	love.graphics.setFont(titleFont)
	text = "Scene Selection"
	love.graphics.print(text,320-titleFont:getWidth(text)/2,5)

	local height = 100
	local line = love.graphics.newImage("assets/Character/"..Character.select_line..".png")
	love.graphics.draw(line, 170,height+40*(choice-2))

	love.graphics.setFont(subFont)
	print(tostring(Character.scenelist[1].scene_num))
	for i=2,1+Character.scenelist[1].scene_num do
		text = Character.scenelist[i].Title
		love.graphics.print(text,200,height)
		height = height + 40
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

	if love.keyboard.isDown('enter') then
		isSceneSelect = false
		isPlayScene = true
		Scene = Character.scenelist[choice].File
	end
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