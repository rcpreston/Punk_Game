debug = true

bump = require 'bump'
JSON = require 'json'
anim8 = require 'anim8'
gamera = require 'gamera'
shakycam = require 'shakycam'
class = require 'middleclass'
entity = require 'entity'

local Map = class('Map')

function Map:initialize(map_info,camera)
	
	local a = love.filesystem.read("assets/Map/"..map_info.folder.."/walls.js")
	local wall_list = JSON:decode(a)
	a = love.filesystem.read("assets/Map/"..map_info.folder.."/portals.js")
	local portal_list = JSON:decode(a)
	local back_list = {0,0}
	back_list[1] = tonumber(map_info.back_item[1].num)
	for j=2,back_list[1]+1 do
		back_list[j] = {
			image = love.graphics.newImage(map_info.back_item[j].image),
			speed = tonumber(map_info.back_item[j].speed),
			x = 0
		}
	end
	self.portals = {}
	self.portals[1] = tonumber(portal_list[1].num)
	for j=2,self.portals[1]+1 do
		self.portals[j] = {
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
	self.walls = {}
	self.walls[1] = tonumber(wall_list[1].num)
	for j=2,self.walls[1]+1 do
		self.walls[j] = {
			x = tonumber(wall_list[j].x_loc),
			y = tonumber(wall_list[j].y_loc),
			width = tonumber(wall_list[j].width),
			height = tonumber(wall_list[j].height)
		}
	end
	self.bg = love.graphics.newImage(map_info.bg)
	self.bg_x = 0
	self.floor = love.graphics.newImage(map_info.floor)
	self.floor_spd = tonumber(map_info.floor_speed)
	self.floor_x = 0
	self.front = love.graphics.newImage(map_info.front)
	self.front_spd = tonumber(map_info.front_speed)
	self.front_x = 0
	self.back_list = back_list
	self.npc_list = map_info.npcs
	self.camera = camera

	-- Add things to collision world
	self.world = bump.newWorld()
	self.player = Player:new(self.world)
	for i=2,self.walls[1]+1 do
		self.world:add(self.walls[i],self.walls[i].x,
			self.walls[i].y,self.walls[i].width,
			self.walls[i].height)
	end

	self.objects = {}
	self.objects[1] = tonumber(map_info.objects[1].num)
	for j=2,self.objects[1]+1 do
		self.objects[j] = entity:new(self.world,map_info.objects[j])
	end
	--for i=2,self.objects[1]+1 do
	--	self.world:add(self.objects[i],
	--		self.objects[i].coll_x, self.objects[i].coll_y,
	--		self.objects[i].w, self.objects[i].h)
	--end

end

function Map:checkPortal()
	local isPortal = false
	local map_num = 0
	local portal_name = nil


	return isPortal,map_num,portal_name
end

function Map:update(dt)
	if love.keyboard.isDown('enter','x') then
		--local actualX, actualY, cols, len = self.world:check(self.player, goalX, goalY, <filter>)
	end
	self.player:update(dt)

end

function Map:draw()
	love.graphics.draw(self.bg,self.bg_x,0)
	for i=2, self.back_list[1]+1 do
		love.graphics.draw(self.back_list[i].image,self.back_list[i].x,0)
	end
	love.graphics.draw(self.floor,self.floor_x,0)
	self.player:draw()
	for i=2, self.objects[1]+1 do
		if self.player.coll_y > self.objects[i].coll_y then
			--love.graphics.draw(self.objects[i].image,self.objects[i].x,self.objects[i].y)
			self.objects[i]:draw()
			self.player:draw()
		else 
			self.objects[i]:draw()
			--love.graphics.draw(self.objects[i].image,self.objects[i].x,self.objects[i].y)
		end
		
	end
	love.graphics.draw(self.front,self.front_x,0)
end

function Map:move_L()
end

function Map:move_R()
end

function Map:sort()
	num = objects[1].num

	for 

return Map