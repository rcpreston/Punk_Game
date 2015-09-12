-- Window Configuration
function love.conf(t)
	t.title = "Punks R Us" -- Title of game
	t.version = "0.9.2" -- LOVE version game is made with
	t.window.width = 640
	t.window.height = 480

	love.filesystem.setIdentity("Punk_Saves")

	-- For debugging
	t.console = true
end