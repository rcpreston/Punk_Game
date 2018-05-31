bump = require 'bump'
JSON = require 'json'
anim8 = require 'anim8'
gamera = require 'gamera'
shakycam = require 'shakycam'
class = require 'middleclass'

local Entity = class('Entity')

function Entity:initialize(world,info)
	self.x = tonumber(info.x)
	self.y = tonumber(info.y)
	self.w = tonumber(info.w)
	self.h = tonumber(info.h)
	self.coll_x = tonumber(info.coll_x)
	self.coll_y = tonumber(info.coll_y)
	self.image = love.graphics.newImage(info.model)

	world:add(self,
			self.coll_x, self.coll_y,
			self.w, self.h)
end

function Entity:update(dt)
end

function Entity:draw()
	love.graphics.draw(self.image,self.x,self.y)
end

return Entity