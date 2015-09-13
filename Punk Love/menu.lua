-- Menu stuff

a= love.filesystem.read("assets/Menu/options.js")
print(a)
options = JSON:decode(a)
choice = 2
menu = "main"
sub = 0
timer = 0.2

function draw()
	background = love.graphics.newImage("assets/Menu/background.png")
	love.graphics.draw(background,0,0)
	if menu == "main" then
		if choice == tonumber(options[1].num+2) then
			-- Draw the selection rectangle on the back button
		else
			-- Draw selection rectangle on menu option
		end
		for i=2,1+tonumber(options[1].num) do
			text = options[i].name
		end
	elseif menu == "sub" then
		if choice == tonumber(options[sub].list[1].num+2) then
			-- Draw the selection rectangle on the back button
		else
			-- Draw selection rectangle on menu option
		end
		for i=2,1+tonumber(options[sub].list[1].num) do
			text = options[sub].list[i].name
		end
	end
end

function update(dt)
	timer = timer - dt
	if love.keyboard.isDown('up','w') and timer <= 0 then
		timer = 0.2

	end
end