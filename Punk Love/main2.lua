debug = true
require 'middleclass'
bump = require 'bump'
JSON = require 'json'
anim8 = require 'anim8'
gamera = require 'gamera'
shakycam = require 'shakycam'
Map = require 'map'
Player = require 'player'

player = nil
map = nil
camera = nil



function love.load(arg)
	love.graphics.setDefaultFilter('nearest','nearest')
	--camera = shakycam.new(gamera_cam)
	camera = gamera.new(0,0,1000,480)
	camera:setWindow(0,0,640,480)
	local a = love.filesystem.read("assets/Scene/Beanie1/map_info.js")
	local map_info = JSON:decode(a)
	map = Map:new(map_info[2],camera)

	timer = 0.2
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
	choice = 2
end

function love.update(dt)
	--charselectUpdate(dt)
	map:update(dt)
	camera:setPosition(map.player:getCenter())
	camera:setScale(2.0)

	
end

function love.draw(dt)
	--charselectDraw()
	camera:draw(function(l,t,w,h)
		map:draw()
	end)
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
		--isCharSelect = false
		--isSceneSelect = true
		Character = char_list[choice]
		image = love.graphics.newImage('assets/Character/'..char_list[choice].model..'.png')
		choice = 2
		timer = 0.2
	end
end