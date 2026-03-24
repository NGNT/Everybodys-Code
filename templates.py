# Enhanced user-friendly features for Everybody's Code

BEGINNER_TEMPLATES = {
"Basic Mod Structure": """
-- Basic Teardown Multiplayer Mod Template
-- Created with Everybody's Code

function shared.init()
    -- Shared initialization (runs on both server and clients)
    -- Use for shared data that both server and clients need
end

function server.init()
    -- Server-side initialization (runs once on the host)
    DebugPrint("My mod server is starting!")

    -- Example: Find objects and set up server state
    -- myObject = FindBody("my_object")
    -- gameState = 1
end

function client.init()
    -- Client-side initialization (runs once on each client)
    DebugPrint("My mod client is starting!")

    -- Load client-side resources (sounds, etc.)
    -- mySound = LoadSound("path/to/sound.ogg")
end

function server.tick(dt)
    -- Server logic (runs every frame on host)
    -- Handle physics, game rules, object interactions

    -- Sync important state to clients via shared table
    -- shared.gameState = gameState
    -- shared.playerCount = #GetAllPlayers()

    -- Example: Check all players for input
    -- local players = GetAllPlayers()
    -- for i = 1, #players do
    --     local player = players[i]
    --     if InputPressed("interact", player) then
    --         -- Handle player interaction
    --     end
    -- end
end

function client.tick(dt)
    -- Client logic (runs every frame on each client)
    -- Handle client-specific input, effects, sounds

    -- Read synchronized state from shared table
    -- local currentGameState = shared.gameState or 1
end

function client.draw()
    -- UI drawing (runs on each client when rendering UI)
    -- Draw text, HUD elements, etc.

    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("My Mod is Running!")
    UiPop()
end
""",

"Simple Physics Mod": """
-- Physics Fun Multiplayer Mod Template

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Physics mod server loaded!")

    -- Find objects to interact with
    explosiveObjects = FindBodies("explosive")

    -- Sync state to clients
    shared.explosionCount = 0
end

function client.init()
    DebugPrint("Physics mod client loaded!")

    -- Load explosion sound on each client
    explosionSound = LoadSound("MOD/sounds/explosion.ogg")
end

function server.tick(dt)
    -- Server handles the physics and game logic

    -- Check all players for space key press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get player's camera for explosion position
            local camera = GetPlayerCameraTransform(player)
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local pos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                Explosion(pos, 2.0)  -- Explosion where player is looking

                -- Update explosion counter
                shared.explosionCount = (shared.explosionCount or 0) + 1

                DebugPrint("Player " .. player .. " created explosion #" .. shared.explosionCount)
            end
        end
    end
end

function client.tick(dt)
    -- Client handles local effects and sounds
    -- Note: Explosions are already handled by server
end

function client.draw()
    -- Show instructions and explosion count
    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("Press SPACE to explode where you're looking!")

        UiTranslate(0, 30)
        local count = shared.explosionCount or 0
        UiText("Total explosions: " .. count)
    UiPop()
end
""",

"Interactive Object Mod": """-- Interactive Object Multiplayer Mod Template

local interactiveObject = nil

function shared.init()
    -- Shared initialization
end

function server.init()
    -- Find an object to interact with on the server
    interactiveObject = FindBody("interactive")
    if interactiveObject == 0 then
        DebugPrint("No object named 'interactive' found!")
    else
        DebugPrint("Found interactive object!")

        -- Set up interaction tag
        local shapes = GetBodyShapes(interactiveObject)
        if #shapes > 0 then
            SetTag(shapes[1], "interact", "Activate")
        end
    end

    -- Server state
    shared.objectActivated = false
    shared.activationCount = 0
end

function client.init()
    DebugPrint("Interactive mod client ready!")

    -- Load interaction sound
    activationSound = LoadSound("MOD/sounds/activate.ogg")
end

function server.tick(dt)
    -- Server handles object state and physics
    if interactiveObject and interactiveObject ~= 0 then
        -- Check all players for interaction
        local players = GetAllPlayers()
        for i = 1, #players do
            local player = players[i]
            local interactShape = GetPlayerInteractShape(player)

            -- Check if player is interacting with our object
            if interactShape ~= 0 then
                local shapeBody = GetShapeBody(interactShape)
                if shapeBody == interactiveObject and InputPressed("interact", player) then
                    -- Player activated the object
                    SetBodyVelocity(interactiveObject, Vec(0, 5, 0))  -- Make it jump

                    -- Update shared state
                    shared.objectActivated = true
                    shared.activationCount = (shared.activationCount or 0) + 1

                    DebugPrint("Player " .. player .. " activated object! (Total: " .. shared.activationCount .. ")")

                    -- Reset activation flag after a short time
                    -- (This could be improved with a timer system)
                end
            end
        end

        -- Reset activation flag (simple approach)
        if shared.objectActivated then
            shared.objectActivated = false
        end
    end
end

function client.tick(dt)
    -- Client handles local effects
    if shared.objectActivated and activationSound then
        PlaySound(activationSound, GetBodyTransform(interactiveObject).pos, 1.0)
    end
end

function client.draw()
    -- Show interaction hints and statistics
    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("Find the 'interactive' object and press E to activate it!")

        UiTranslate(0, 30)
        local count = shared.activationCount or 0
        UiText("Times activated: " .. count)

        -- Show interaction prompt when looking at object
        if interactiveObject and interactiveObject ~= 0 then
            local camera = GetCameraTransform()
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 10)

            if hit and GetShapeBody(shape) == interactiveObject then
                UiPush()
                    UiAlign("center middle")
                    UiTranslate(UiWidth()/2, UiHeight()/2)
                    UiColor(1, 1, 0)  -- Yellow highlight
                    UiText("Press E to activate")
                UiPop()
            end
        end
    UiPop()
end
""",

"Explosion Mod": """
-- Simple Explosion Template
-- Create explosions when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local explosionPos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                Explosion(explosionPos, 3.0)  -- Big explosion
            end
        end
    end
end
""",

"Paint Mod": """
-- Simple Paint Template
-- Paint surfaces when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local paintPos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                local paintColor = {math.random(), math.random(), math.random()}  -- Random color
                Paint(paintPos, 1.0, paintColor[1], paintColor[2], paintColor[3])  -- Paint 1m radius
            end
        end
    end
end
""",

"Shape Breaking Mod": """
-- Simple Shape Breaking Template
-- Break shapes when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit and shape ~= 0 then
                -- Split the shape to break it apart
                local newShapes = SplitShape(shape, true)

                -- Apply force to broken pieces
                for j = 1, #newShapes do
                    local shapeBody = GetShapeBody(newShapes[j])
                    if IsHandleValid(shapeBody) then
                        SetBodyDynamic(shapeBody, true)
                        local randomForce = Vec(
                            (math.random() - 0.5) * 20,
                            math.random() * 10 + 5,
                            (math.random() - 0.5) * 20
                        )
                        ApplyBodyImpulse(shapeBody, GetBodyTransform(shapeBody).pos, randomForce)
                    end
                end
            end
        end
    end
end
""",

"Object Launching Mod": """
-- Simple Object Launching Template
-- Launch objects when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit and shape ~= 0 then
                local shapeBody = GetShapeBody(shape)
                if IsHandleValid(shapeBody) then
                    -- Make object dynamic and launch it
                    SetBodyDynamic(shapeBody, true)
                    local launchForce = VecScale(camera.fwd, 500)  -- Strong push forward
                    ApplyBodyImpulse(shapeBody, GetBodyTransform(shapeBody).pos, launchForce)
                end
            end
        end
    end
end
""",

"Vehicle Control Mod": """
-- Simple Vehicle Control Template
-- Find a vehicle and set basic properties

local vehicle = nil

function server.init()
    -- Find any vehicle in the scene
    vehicle = FindVehicle("", true)
end

function server.tick(dt)
    -- Set basic vehicle properties if we found one
    if vehicle ~= 0 then
        SetVehicleParam(vehicle, "topspeed", 30)  -- Set top speed
        SetVehicleParam(vehicle, "acceleration", 15)  -- Set acceleration
    end
end
""",

"Lighting & Visual Effects Mod": """
-- Simple Light Control Template
-- Find a light and turn it on

local light = nil

function server.init()
    -- Find any light in the scene
    light = FindLight("", true)
end

function server.tick(dt)
    -- Turn on the light if we found one
    if light ~= 0 then
        SetLightEnabled(light, true)
    end
end
""",

"Particle Effects Mod": """
-- Simple Chimney Smoke Template
-- Create smoke that goes up straight and gradually cones outward

function server.tick(dt)
    -- Check for spacebar press to create smoke
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            local playerPos = GetPlayerTransform(player).pos
            shared.createSmoke = playerPos
        end
    end
end

function client.tick(dt)
    -- Create chimney smoke particles
    if shared.createSmoke then
        local smokePos = shared.createSmoke

        -- Spawn smoke particles
        for i = 1, 5 do
            ParticleReset()
            ParticleType("smoke")
            ParticleColor(0.7, 0.7, 0.7)  -- Gray smoke
            ParticleAlpha(0.5, 0.0)  -- Fade out
            ParticleRadius(0.1, 0.6)  -- Grow larger as it rises
            ParticleGravity(-1)  -- Float upward

            -- Start straight up, gradually cone outward
            local outward = (math.random() - 0.5) * 0.5  -- Small random outward drift
            local smokeVel = Vec(outward, 3, outward)  -- Mostly upward

            SpawnParticle(smokePos, smokeVel, 3.0)  -- 3 second lifetime
        end

        shared.createSmoke = nil
    end
end
""",

"Trigger Zone Mod": """
-- Simple Trigger Zone Template
-- Detect when players enter and exit a trigger

local trigger = nil

function server.init()
    -- Find any trigger in the scene
    trigger = FindTrigger("", true)
end

function server.tick(dt)
    -- Check if players are in the trigger
    if trigger ~= 0 then
        local players = GetAllPlayers()
        for i = 1, #players do
            local player = players[i]
            local playerPos = GetPlayerTransform(player).pos
            local inZone = IsPointInTrigger(trigger, playerPos)

            -- Update shared state
            shared["player" .. player .. "_inzone"] = inZone
        end
    end
end

function client.draw()
    -- Show trigger status
    local localPlayer = GetLocalPlayer()
    local inZone = shared["player" .. localPlayer .. "_inzone"]

    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        if inZone then
            UiColor(0, 1, 0)  -- Green when in zone
            UiText("IN TRIGGER ZONE")
        else
            UiColor(1, 0, 0)  -- Red when outside
            UiText("Outside trigger zone")
        end
    UiPop()
end
""",

"Custom Tool Mod": """
-- Simple Custom Tool Template
-- Register a custom tool

function server.init()
    -- Register a custom tool
    RegisterTool("my_tool", "My Tool", "MOD/vox/my_tool.vox", 1)
    SetBool("game.tool.my_tool.enabled", true)
end

function server.tick(dt)
    -- Give the tool to new players
    local addedPlayers = GetAddedPlayers()
    for i = 1, #addedPlayers do
        local player = addedPlayers[i]
        SetToolEnabled("my_tool", true, player)
    end
end
""",

"Fire & Heat Mod": """
-- Simple Fire Mod Template
-- Spawn fire when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local firePos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                SpawnFire(firePos)  -- Start a fire
            end
        end
    end
end
""",

"Joint Spinning Mod": """
-- Simple Joint Spinning Mod Template
-- Find a joint and make it spin

local joint = nil

function server.init()
    -- Find any joint in the scene
    joint = FindJoint("", true)
end

function server.tick(dt)
    -- Make the joint spin if we found one
    if joint ~= 0 then
        SetJointMotor(joint, 10)  -- Spin at speed 10
    end
end
""",

"Hole Making Mod": """
-- Simple Hole Making Template
-- Make holes when you press spacebar

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Get where player is looking
            local camera = GetPlayerCameraTransform(player)
            local hit, dist = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local holePos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                MakeHole(holePos, 2.0, 2.0, 2.0)  -- 2m cube hole
            end
        end
    end
end
""",

"Sound & Music Mod": """
-- Simple Sound Mod Template
-- Load a sound and play it when you press a button

local mySound = nil

function client.init()
    -- Load a sound file
    mySound = LoadSound("MOD/sounds/explosion.ogg")
end

function server.tick(dt)
    -- Check for spacebar press
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if InputPressed("space", player) then
            -- Tell clients to play sound
            shared.playSound = true
        end
    end
end

function client.tick(dt)
    -- Play sound when triggered
    if shared.playSound and mySound then
        PlaySound(mySound, GetCameraTransform().pos, 1.0)
        shared.playSound = false
    end
end
"""
}

COMMON_PATTERNS = {

"Multiplayer Input Check": {
"description": "Properly check input from all players in multiplayer",
"explanation": "In multiplayer, always loop through all players when checking input. Use GetAllPlayers() and specify the player index in InputPressed().",
"setup_code": "-- Put this in server.tick(dt)",
"usage_code": """
local players = GetAllPlayers()
for i = 1, #players do
    local player = players[i]
    if InputPressed("interact", player) then
        DebugPrint("Player " .. player .. " pressed interact!")
        -- Handle the player's action here
    end
end""",
    },

"Sync Server and Client": {
"description": "Synchronize server state to all clients using shared table",
"explanation": "Use the 'shared' table to sync server state to clients. Server writes to it, clients read from it with safe defaults.",
"setup_code": "-- Server writes to shared table in server.tick(dt)",
"usage_code": """
-- Server side (in server.tick):
shared.gameState = gameState
shared.playerCount = #GetAllPlayers()
shared.score = currentScore

-- Client side (in client.tick or client.draw):
local state = shared.gameState or 1
local players = shared.playerCount or 0
local score = shared.score or 0""",
    },

"Player Interaction Detection": {
"description": "Detect when players interact with specific objects",
"explanation": "Use GetPlayerInteractShape() to check what object each player is looking at, then check if they pressed interact.",
"setup_code": "-- Set up interaction tag in server.init()\n-- SetTag(myShape, \"interact\", \"Press E\")",
"usage_code": """
local players = GetAllPlayers()
for i = 1, #players do
    local player = players[i]
    local interactShape = GetPlayerInteractShape(player)
    if interactShape == myTargetShape and InputPressed("interact", player) then
        -- Player interacted with the target object
        DebugPrint("Player " .. player .. " interacted!")
    end
end""",
    },

"Cooldown Timer": {
"description": "Create a timer that prevents actions from happening too frequently",
"explanation": "This pattern prevents spam by setting a cooldown time. The action can only happen when enough time has passed.",
"setup_code": "local cooldownTime = 0",
"usage_code": """
if GetTime() > cooldownTime then
    -- Do the action
    DebugPrint("Action executed!")
    cooldownTime = GetTime() + 2.0  -- Wait 2 seconds before next action
end""",
    },

"Make a Switch": {
"description": "Create an on/off switch with a key",
"explanation": "This creates a toggle that switches between true/false when you press T. It includes a small delay to prevent accidental double-presses.",
"setup_code": "local isToggled = false\nlocal lastToggleTime = 0",
"usage_code": """
if InputPressed("t") and GetTime() > lastToggleTime + 0.2 then
    isToggled = not isToggled
    lastToggleTime = GetTime()
    DebugPrint("Toggle is now: " .. (isToggled and "ON" or "OFF"))
end""",   
    },

"Safe Player Camera Access": {
"description": "Get player camera position safely in server code",
"explanation": "In server code, use GetPlayerCameraTransform(player) instead of GetCameraTransform() to safely access each player's camera.",
"setup_code": "-- Use in server.tick(dt) to get player camera",
"usage_code": """
local players = GetAllPlayers()
for i = 1, #players do
    local player = players[i]
    local camera = GetPlayerCameraTransform(player)
    local playerPos = camera.pos
    -- Now you can use playerPos for distance checks, etc.
end""",
    },

"Make something follow a Player": {
"description": "Make an object smoothly follow the player",
"explanation": "This makes an object named 'follower' chase the player by calculating the direction and applying velocity.",
"setup_code": "local followObject = FindBody(\"follower\")",
"usage_code": """
if followObject and followObject ~= 0 then
    local playerPos = GetCameraTransform().pos
    local objectPos = GetBodyTransform(followObject).pos
    local direction = VecNormalize(VecSub(playerPos, objectPos))
    local speed = 5.0
    SetBodyVelocity(followObject, VecScale(direction, speed))
end""", 
    },

"Make a safe UI": {
"description": "Draw UI that works on all screen sizes and ratios",
"explanation": "Use UiSafeMargins() to get safe drawing area that works on all screen ratios. Always use UiPush/UiPop to save/restore UI state.",
"setup_code": "-- Put this in client.draw() function",
"usage_code": """
UiPush()
    -- Use safe margins for different screen ratios
    local x0, y0, x1, y1 = UiSafeMargins()
    UiTranslate(x0 + 50, y0 + 50)  -- 50px from safe edge
    UiColor(1, 1, 1)
    UiText("Score: " .. score)
UiPop()""",
    },

"Check for an Object": {
"description": "Safely check if game objects still exist before using them",
"explanation": "Always check if handles are valid before using them. Objects can be destroyed during gameplay, making their handles invalid.",
"setup_code": "local myObject = FindBody(\"my_object\")",
"usage_code": """
if myObject and myObject ~= 0 and IsHandleValid(myObject) then
    -- Safe to use myObject
    local transform = GetBodyTransform(myObject)
    -- Do something with the object
else
    -- Object doesn't exist or was destroyed
    DebugPrint("Object no longer exists!")
end""",
    },

"Detect when a Player Joins/Leaves": {
"description": "Detect when players join or leave the session",
"explanation": "Use GetAddedPlayers() and GetRemovedPlayers() to react to player changes. This is called every frame for new/removed players.",
"setup_code": "-- Put this in server.tick(dt)",
"usage_code": """
local addedPlayers = GetAddedPlayers()
for i = 1, #addedPlayers do
    local player = addedPlayers[i]
    DebugPrint("Player " .. player .. " joined!")
    -- Initialize player state, give spawn items, etc.
    shared.playerJoined = player
end

local removedPlayers = GetRemovedPlayers()
for i = 1, #removedPlayers do
    local player = removedPlayers[i]
    DebugPrint("Player " .. player .. " left!")
    -- Clean up player data
    shared.playerLeft = player
end""",
    },

"Call the server": {
"description": "Call server functions from client to request validation or actions",
"explanation": "Use ServerCall() on client to invoke server functions. Useful for validated actions like tool usage or score updates.",
"setup_code": "-- Client: Call in client.tick()\n-- Server: Define function in server section",
"usage_code": """
-- CLIENT SIDE (in client.tick):
function client.tick()
	if UiTextButton("I am Ready") then
		ServerCall("server.setPlayerReady", GetLocalPlayer()) 
	end
end

-- SERVER SIDE (define this function):
function server.setPlayerReady(playerId)
	shared.playersReady[playerId] = true
end""",
	},

"Call the client": {
"description": "Call client functions from server to trigger client-side effects",
"explanation": "Use ClientCall() on server to invoke client functions. Useful for triggering client-specific effects, sounds, or UI updates.",
"setup_code": "-- Server: Call in server.tick()\n-- Client: Define function in client section",
"usage_code": """
-- SERVER SIDE (in server.tick):
function server.tick(dt)
	local players = GetAllPlayers()
	for i = 1, #players do
		local player = players[i]
		if InputPressed("space", player) then
			-- Trigger effect on all clients
			ClientCall("client.playExplosionEffect", player, GetPlayerTransform(player).pos)
		end
	end
end

-- CLIENT SIDE (define this function):
function client.playExplosionEffect(playerId, position)
	-- Play sound effect
	PlaySound(explosionSound, position, 1.0)
	-- Show screen shake or particles
	DebugPrint("Player " .. playerId .. " caused explosion!")
end""",
	},

"Make a Custom Event": {
"description": "Post and handle custom events for inter-script communication",
"explanation": "Use PostEvent() to broadcast events and GetEvent() to retrieve them. Great for decoupling game systems.",
"setup_code": "-- Can post events from anywhere, handle them in server.tick()",
"usage_code": """
-- Post an event (from anywhere):
PostEvent("playerscored", playerId, pointsEarned)

-- Handle events (in server.tick):
local eventCount = GetEventCount("playerscored")
for i = 1, eventCount do
    local scoringPlayer, points = GetEvent("playerscored", i)
    DebugPrint("Player " .. scoringPlayer .. " scored " .. points .. " points!")
    shared.totalScore = (shared.totalScore or 0) + points
end""",
    },

"Win Condition / Goal Detection": {
"description": "Detect when players reach a goal or win condition",
"explanation": "Check if player position is in a trigger/goal area. Update shared state when victory occurs.",
"setup_code": "local goalTrigger = FindTrigger(\"goal\")",
"usage_code": """
function server.tick(dt)
    if shared.winner == -1 then
        local players = GetAllPlayers()
        for i = 1, #players do
            local player = players[i]
            local playerTransform = GetPlayerTransform(player)
            if IsPointInTrigger(goalTrigger, playerTransform.pos) then
                shared.winner = player
                shared.winTime = GetTime()
                DebugPrint("Player " .. player .. " reached the goal!")
            end
        end
    end
end""",
    },

"Track a Player's Stats": {
"description": "Track individual state for each player (health, ammo, status)",
"explanation": "Maintain a table mapping player IDs to their state. Initialize on join, clean up on leave.",
"setup_code": "local playerStates = {}",
"usage_code": """
function server.tick(dt)
    -- Initialize new players
    for i = 1, #GetAddedPlayers() do
        local player = GetAddedPlayers()[i]
        playerStates[player] = {
            health = 100,
            ammo = 60,
            lastActionTime = GetTime()
        }
    end

    -- Clean up leaving players
    for i = 1, #GetRemovedPlayers() do
        local player = GetRemovedPlayers()[i]
        playerStates[player] = nil
    end

    -- Update each player's state
    for player, state in pairs(playerStates) do
        -- Modify state based on game logic
        state.health = math.max(0, state.health - 1)
        shared.playerData = playerStates  -- Sync to clients
    end
end""",
    },

"Make some Particles": {
"description": "Create visual effects using particle system with custom properties",
"explanation": "Use ParticleReset() to configure, then SpawnParticle() to emit. Configure color, size, gravity, drag.",
"setup_code": "-- Can be called from server.tick() or client.tick()",
"usage_code": """
-- Explosion fire particles:
ParticleReset()
ParticleType("fire")
ParticleColor(1, 0.9, 0.8, 1, 0.5, 0.4)  -- Start bright, fade to orange
ParticleAlpha(0.5, 0.0)  -- Fade from 0.5 to 0
ParticleRadius(0.1, 0.5)  -- Grow from 0.1 to 0.5
ParticleEmissive(10, 0)  -- Glow effect
SpawnParticle(explosionPosition, VecScale(rndVec(1), 5), 0.5)

-- Smoke particles:
ParticleReset()
ParticleType("smoke")
ParticleDrag(0)
ParticleGravity(-2, -4)  -- Float upward
ParticleColor(1, 1, 1)
ParticleAlpha(0.5, 0.0, "linear", 0.05)
SpawnParticle(smokePosition, Vec(0, 2, 0), 1.0)""",
    },

"Register A Custom Tool": {
"description": "Register and manage a custom tool with ammo and properties",
"explanation": "Use RegisterTool() in init, then manage ammo and enabled state per player.",
"setup_code": "-- In server.init():\nRegisterTool(\"customtool\", \"Tool Name\", \"MOD/vox/tool.vox\", toolGroup)",
"usage_code": """
function server.init()
    RegisterTool("lasergun", "Laser Gun", "MOD/vox/lasergun.vox", 1)
    SetToolAmmoPickupAmount("lasergun", 30)
    SetBool("game.tool.lasergun.enabled", true)
end

function server.tick(dt)
    -- Initialize new players with the tool
    local addedPlayers = GetAddedPlayers()
    for i = 1, #addedPlayers do
        local player = addedPlayers[i]
        SetToolEnabled("lasergun", true, player)
        SetToolAmmo("lasergun", 100, player)
    end

    -- Check all players using the tool
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        if GetPlayerTool(player) == "lasergun" and InputDown("usetool", player) then
            local ammo = GetToolAmmo("lasergun", player)
            if ammo > 0 then
                -- Fire tool logic here
                SetToolAmmo("lasergun", ammo - 1, player)
            end
        end
    end
end""",
    }
}

def get_beginner_template(name):
    return BEGINNER_TEMPLATES.get(name, "")

def get_all_template_names():
    return list(BEGINNER_TEMPLATES.keys())

def get_pattern(name):
    return COMMON_PATTERNS.get(name, {})

def get_all_pattern_names():
    return list(COMMON_PATTERNS.keys())