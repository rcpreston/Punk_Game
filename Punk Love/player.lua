bump = require 'bump'
JSON = require 'json'
anim8 = require 'anim8'
gamera = require 'gamera'
shakycam = require 'shakycam'
class = require 'middleclass'

local Player = class('Player')

function Player:initialize(world)
	image = love.graphics.newImage('assets/Character/bunsheet.png')
  	local g = anim8.newGrid(30, 47, image:getWidth(), image:getHeight())
  	
  	self.y = 200
  	self.coll_y = self.y + 32
  	self.w = 30
  	self.h = 47
  	self.x = 305
  	self.coll_x = self.x + 5
  	self.direction = "D"
  	self.stop = true
  	self.down = anim8.newAnimation(g('1-4',1), 0.2)
  	self.down_s = anim8.newAnimation(g(2,1), 0.2)
  	self.up = anim8.newAnimation(g('1-4',3), 0.2)
  	self.up_s = anim8.newAnimation(g(2,3), 0.2)
  	self.left_w = anim8.newAnimation(g('1-4',2), 0.2)
  	self.left_s = anim8.newAnimation(g(2,2), 0.2)
  	self.left_r = anim8.newAnimation(g('1-6',4), 0.1)
  	self.right_w = anim8.newAnimation(g('1-4',2), 0.2):flipH()
  	self.right_s = anim8.newAnimation(g(2,2), 0.2):flipH()
  	self.right_r = anim8.newAnimation(g('1-6',4), 0.1):flipH()
  	self.world = world
  	self.world:add(self,self.coll_x,self.coll_y,20,15)
  	
end

function Player:update(dt)

	if love.keyboard.isDown('down','s') then
		self.down:update(dt)
		self.coll_y = self.coll_y + 1
		self.direction = "D"
		self.stop = false
	elseif love.keyboard.isDown('up','w') then
		self.up:update(dt)
		self.coll_y = self.coll_y - 1
		self.direction = "U"
		self.stop = false
	elseif love.keyboard.isDown('left','a') then
		self.left_r:update(dt)
		self.direction = "L"
		self.stop = false
		self.coll_x = self.coll_x -2
	elseif love.keyboard.isDown('right','d') then
		self.right_r:update(dt)
		self.direction = "R"
		self.stop = false
		self.coll_x = self.coll_x +2
	else
		self.stop = true
	end
	self.coll_x,self.coll_y = self.world:move(self,self.coll_x,self.coll_y)
	self.y = self.coll_y - 32
	self.x = self.coll_x -5
end

function Player:draw()
	if self.direction == "D" then
		if not self.stop then
			self.down:draw(image,self.x,self.y)
		else
		    self.down_s:draw(image,self.x,self.y)
		end
	elseif self.direction == "U" then
	    if not self.stop then
	        self.up:draw(image,self.x,self.y)
	    else
	        self.up_s:draw(image,self.x,self.y)
	    end
	elseif self.direction == "L" then
	    if not self.stop then
	        self.left_r:draw(image,self.x,self.y)
	    else
	        self.left_s:draw(image,self.x,self.y)
	    end
	elseif self.direction == "R" then
	    if not self.stop then
	        self.right_r:draw(image,self.x,self.y)
	    else
	        self.right_s:draw(image,self.x,self.y)
	    end
	end
end

function Player:getCenter()
  return self.x + self.w / 2,
         self.y + self.h / 2
end

return Player