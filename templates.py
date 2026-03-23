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

"Environmental Destruction Mod": """
-- Environmental Destruction Multiplayer Mod Template
-- Shows how to use MakeHole, Paint, Explosion, and shape manipulation

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Environmental destruction mod server loaded!")

    -- Server tracks destruction events
    shared.destructionEvents = {}
    shared.destructionCount = 0
end

function client.init()
    DebugPrint("Environmental destruction mod client loaded!")
end

function server.tick(dt)
    -- Server handles destruction logic

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        local camera = GetPlayerCameraTransform(player)

        -- Press SPACE to explode where player is looking
        if InputPressed("space", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit then
                local pos = VecAdd(camera.pos, VecScale(TransformToParentVec(camera, Vec(0, 0, -1)), dist))
                Explosion(pos, 3.0)  -- Big explosion

                shared.destructionCount = (shared.destructionCount or 0) + 1
                DebugPrint("Player " .. player .. " created explosion #" .. shared.destructionCount)
            end
        end

        -- Press H to make hole where player is looking
        if InputPressed("h", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit then
                local pos = VecAdd(camera.pos, VecScale(TransformToParentVec(camera, Vec(0, 0, -1)), dist))
                MakeHole(pos, 2.0, 2.0, 2.0)  -- 2m cube hole

                DebugPrint("Player " .. player .. " made a hole!")
            end
        end

        -- Press P to paint where player is looking
        if InputPressed("p", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit then
                local pos = VecAdd(camera.pos, VecScale(TransformToParentVec(camera, Vec(0, 0, -1)), dist))
                local paintColor = {math.random(), math.random(), math.random()}  -- Random color
                Paint(pos, 1.0, paintColor[1], paintColor[2], paintColor[3])  -- Paint 1m radius

                DebugPrint("Player " .. player .. " painted the surface!")
            end
        end

        -- Press B to break shapes where player is looking
        if InputPressed("b", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit and shape ~= 0 then
                -- Split the shape to break it apart
                local newShapes = SplitShape(shape, true)  -- Remove small chunks

                if #newShapes > 1 then
                    -- Apply some force to the broken pieces
                    for j = 1, #newShapes do
                        local shapeBody = GetShapeBody(newShapes[j])
                        if IsHandleValid(shapeBody) then
                            SetBodyDynamic(shapeBody, true)  -- Make it dynamic
                            local randomForce = Vec(
                                (math.random() - 0.5) * 20,
                                math.random() * 10 + 5,  -- Always up
                                (math.random() - 0.5) * 20
                            )
                            ApplyBodyImpulse(shapeBody, GetBodyTransform(shapeBody).pos, randomForce)
                        end
                    end

                    DebugPrint("Player " .. player .. " broke shape into " .. #newShapes .. " pieces!")
                else
                    DebugPrint("Player " .. player .. " hit unbreakable object!")
                end
            end
        end

        -- Press F to add fire where player is looking
        if InputPressed("f", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit then
                local pos = VecAdd(camera.pos, VecScale(TransformToParentVec(camera, Vec(0, 0, -1)), dist))
                SpawnFire(pos)  -- Start a fire

                DebugPrint("Player " .. player .. " started a fire!")
            end
        end

        -- Press G to launch objects where player is looking
        if InputPressed("g", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, TransformToParentVec(camera, Vec(0, 0, -1)), 50)

            if hit and shape ~= 0 then
                local shapeBody = GetShapeBody(shape)
                if IsHandleValid(shapeBody) then
                    -- Make object dynamic and launch it
                    SetBodyDynamic(shapeBody, true)
                    local launchDirection = TransformToParentVec(camera, Vec(0, 0, -1))
                    local launchForce = VecScale(launchDirection, 500)  -- Strong push
                    ApplyBodyImpulse(shapeBody, GetBodyTransform(shapeBody).pos, launchForce)

                    DebugPrint("Player " .. player .. " launched an object!")
                end
            end
        end
    end
end

function client.tick(dt)
    -- Client handles local destruction effects
    -- Most destruction happens on server for consistency
end
""",

"Vehicle Control Mod": """
-- Vehicle Control Multiplayer Mod Template
-- Shows how to find, control, and modify vehicles

-- Vehicle handles (found in server.init)
local vehicles = {}
local aiVehicle = nil

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Vehicle control mod server loaded!")

    -- Find all vehicles in the scene
    vehicles = FindVehicles("", true)  -- Find all vehicles
    DebugPrint("Found " .. #vehicles .. " vehicles in scene")

    -- Find a specific vehicle for AI control
    aiVehicle = FindVehicle("ai_car", true)  -- Look for vehicle tagged "ai_car"
    if aiVehicle == 0 then
        -- If no "ai_car" found, use the first vehicle
        aiVehicle = vehicles[1] or 0
    end

    -- Server state
    shared.aiControlled = false
    shared.vehicleCount = #vehicles
end

function client.init()
    DebugPrint("Vehicle control mod client loaded!")
end

function server.tick(dt)
    -- Server handles vehicle logic and control

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]

        -- Press V to enter nearest vehicle
        if InputPressed("v", player) then
            local playerPos = GetPlayerTransform(player).pos
            local nearestVehicle = nil
            local nearestDistance = 999

            -- Find closest vehicle to player
            for j = 1, #vehicles do
                if IsHandleValid(vehicles[j]) then
                    local vehiclePos = GetVehicleTransform(vehicles[j]).pos
                    local distance = VecLength(VecSub(playerPos, vehiclePos))

                    if distance < nearestDistance and distance < 5.0 then  -- Within 5 meters
                        nearestDistance = distance
                        nearestVehicle = vehicles[j]
                    end
                end
            end

            if nearestVehicle then
                SetPlayerVehicle(nearestVehicle, player)
                DebugPrint("Player " .. player .. " entered vehicle!")
            end
        end

        -- Press X to exit current vehicle
        if InputPressed("x", player) then
            local currentVehicle = GetPlayerVehicle(player)
            if currentVehicle ~= 0 then
                SetPlayerVehicle(0, player)  -- 0 = exit vehicle
                DebugPrint("Player " .. player .. " exited vehicle!")
            end
        end

        -- Press C to toggle AI control of a vehicle
        if InputPressed("c", player) then
            shared.aiControlled = not shared.aiControlled
            DebugPrint("Player " .. player .. " toggled AI vehicle: " .. (shared.aiControlled and "ON" or "OFF"))
        end

        -- Press R to repair player's current vehicle
        if InputPressed("r", player) then
            local currentVehicle = GetPlayerVehicle(player)
            if currentVehicle ~= 0 then
                SetVehicleHealth(currentVehicle, 1.0)  -- Full health
                DebugPrint("Player " .. player .. " repaired their vehicle!")
            end
        end

        -- Press T to boost player's current vehicle speed
        if InputPressed("t", player) then
            local currentVehicle = GetPlayerVehicle(player)
            if currentVehicle ~= 0 then
                -- Increase top speed and acceleration
                SetVehicleParam(currentVehicle, "topspeed", 50)  -- Faster top speed
                SetVehicleParam(currentVehicle, "acceleration", 20)  -- Better acceleration
                DebugPrint("Player " .. player .. " boosted their vehicle!")
            end
        end
    end

    -- Simple AI vehicle control - drive in a circle
    if shared.aiControlled and aiVehicle and IsHandleValid(aiVehicle) then
        -- Simple AI: drive forward and turn slightly
        local drive = 0.8  -- 80% throttle forward
        local steering = math.sin(GetTime() * 0.5) * 0.3  -- Gentle turning
        local handbrake = false

        DriveVehicle(aiVehicle, drive, steering, handbrake)
    end
end

function client.tick(dt)
    -- Client can handle local vehicle effects if needed
    -- Most vehicle control happens on server
end
""",

"Lighting & Visual Effects Mod": """
-- Lighting & Visual Effects Multiplayer Mod Template
-- Shows how to manipulate lights, colors, and create atmospheric effects

-- Light handles (found in server.init)
local mainLights = {}
local emissiveShapes = {}

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Lighting effects mod server loaded!")

    -- Find all lights in the scene
    mainLights = FindLights("", true)  -- Find all lights
    DebugPrint("Found " .. #mainLights .. " lights in scene")

    -- Find shapes that can glow (have emissive materials)
    emissiveShapes = FindShapes("glow", true)  -- Find shapes tagged with "glow"
    DebugPrint("Found " .. #emissiveShapes .. " glowing shapes")

    -- Server tracks lighting events
    shared.lightingEvents = {}
    shared.currentMode = "normal"
    shared.flickerTime = 0
end

function client.init()
    DebugPrint("Lighting effects mod client loaded!")
end

function server.tick(dt)
    -- Server handles lighting logic and triggers effects

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]

        -- Press L to cycle through lighting modes
        if InputPressed("l", player) then
            local modes = {"normal", "red_alert", "disco", "flicker"}
            local currentIndex = 1

            -- Find current mode index
            for j = 1, #modes do
                if shared.currentMode == modes[j] then
                    currentIndex = j
                    break
                end
            end

            -- Go to next mode (cycle back to 1 if at end)
            local nextIndex = currentIndex + 1
            if nextIndex > #modes then nextIndex = 1 end

            shared.currentMode = modes[nextIndex]

            table.insert(shared.lightingEvents, {
                type = "mode_change",
                mode = shared.currentMode,
                playerId = player
            })

            DebugPrint("Player " .. player .. " changed lighting to: " .. shared.currentMode)
        end

        -- Press B to make shapes glow brighter
        if InputPressed("b", player) then
            table.insert(shared.lightingEvents, {
                type = "boost_glow",
                playerId = player
            })

            DebugPrint("Player " .. player .. " boosted glow!")
        end

        -- Press O to turn all lights on/off
        if InputPressed("o", player) then
            table.insert(shared.lightingEvents, {
                type = "toggle_all",
                playerId = player
            })

            DebugPrint("Player " .. player .. " toggled all lights!")
        end
    end

    -- Update flicker time for flicker mode
    shared.flickerTime = GetTime()
end

function client.tick(dt)
    -- Client handles the actual lighting effects

    -- Process lighting events from server
    if shared.lightingEvents then
        for i = 1, #shared.lightingEvents do
            local event = shared.lightingEvents[i]

            if event.type == "mode_change" then
                applyLightingMode(event.mode)

            elseif event.type == "boost_glow" then
                -- Make all emissive shapes glow brighter temporarily
                for j = 1, #emissiveShapes do
                    if IsHandleValid(emissiveShapes[j]) then
                        SetShapeEmissiveScale(emissiveShapes[j], 3.0)  -- 3x brighter
                    end
                end

            elseif event.type == "toggle_all" then
                -- Toggle all lights on/off
                local allOff = true
                -- Check if any lights are on
                for j = 1, #mainLights do
                    if IsHandleValid(mainLights[j]) and IsLightActive(mainLights[j]) then
                        allOff = false
                        break
                    end
                end

                -- Set all lights to opposite state
                for j = 1, #mainLights do
                    if IsHandleValid(mainLights[j]) then
                        SetLightEnabled(mainLights[j], allOff)  -- Turn on if all were off
                    end
                end
            end
        end

        -- Clear lighting events after processing (only host clears)
        if GetLocalPlayer() == 1 then
            shared.lightingEvents = {}
        end
    end

    -- Apply current lighting mode effects
    if shared.currentMode then
        applyLightingMode(shared.currentMode)
    end
end

-- Function to apply different lighting modes
function applyLightingMode(mode)
    local time = shared.flickerTime or GetTime()

    if mode == "normal" then
        -- White lights, normal intensity
        for i = 1, #mainLights do
            if IsHandleValid(mainLights[i]) then
                SetLightEnabled(mainLights[i], true)
                SetLightColor(mainLights[i], 1, 1, 1)  -- White
                SetLightIntensity(mainLights[i], 1.0)  -- Normal intensity
            end
        end

        -- Normal glow for emissive shapes
        for i = 1, #emissiveShapes do
            if IsHandleValid(emissiveShapes[i]) then
                SetShapeEmissiveScale(emissiveShapes[i], 1.0)
            end
        end

    elseif mode == "red_alert" then
        -- Red pulsing lights
        local pulse = math.abs(math.sin(time * 2)) * 0.5 + 0.5  -- Pulse between 0.5 and 1

        for i = 1, #mainLights do
            if IsHandleValid(mainLights[i]) then
                SetLightEnabled(mainLights[i], true)
                SetLightColor(mainLights[i], 1, 0.1, 0.1)  -- Red
                SetLightIntensity(mainLights[i], pulse)
            end
        end

    elseif mode == "disco" then
        -- Colorful changing lights
        local r = math.abs(math.sin(time * 3)) 
        local g = math.abs(math.sin(time * 2)) 
        local b = math.abs(math.sin(time * 4))

        for i = 1, #mainLights do
            if IsHandleValid(mainLights[i]) then
                SetLightEnabled(mainLights[i], true)
                -- Each light gets a different color offset
                local offset = i * 1.5
                local lr = math.abs(math.sin(time * 3 + offset))
                local lg = math.abs(math.sin(time * 2 + offset))
                local lb = math.abs(math.sin(time * 4 + offset))
                SetLightColor(mainLights[i], lr, lg, lb)
                SetLightIntensity(mainLights[i], 1.5)  -- Brighter for disco
            end
        end

    elseif mode == "flicker" then
        -- Random flickering lights
        for i = 1, #mainLights do
            if IsHandleValid(mainLights[i]) then
                local flicker = math.random() > 0.3  -- 70% chance to be on
                local intensity = flicker and (0.7 + math.random() * 0.3) or 0  -- Random brightness when on

                SetLightEnabled(mainLights[i], flicker)
                SetLightColor(mainLights[i], 1, 0.9, 0.7)  -- Warm white
                SetLightIntensity(mainLights[i], intensity)
            end
        end
    end
end
""",

"Particle Effects Mod": """
-- Particle Effects Multiplayer Mod Template
-- Shows how to create fire, smoke, sparks, and other visual effects

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Particle effects mod server loaded!")

    -- Server tracks particle events to sync to clients
    shared.particleEvents = {}
    shared.effectCount = 0
end

function client.init()
    DebugPrint("Particle effects mod client loaded!")
end

function server.tick(dt)
    -- Server handles game logic and triggers particle events

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]

        -- Press SPACE for fire explosion at player location
        if InputPressed("space", player) then
            local playerPos = GetPlayerTransform(player).pos

            -- Add fire particle event
            table.insert(shared.particleEvents, {
                type = "fire_explosion",
                position = playerPos,
                playerId = player
            })

            shared.effectCount = (shared.effectCount or 0) + 1
            DebugPrint("Player " .. player .. " created fire explosion!")
        end

        -- Press F for smoke puff
        if InputPressed("f", player) then
            local playerPos = GetPlayerTransform(player).pos

            table.insert(shared.particleEvents, {
                type = "smoke_puff",
                position = VecAdd(playerPos, Vec(0, 1, 0)),  -- Slightly above player
                playerId = player
            })

            DebugPrint("Player " .. player .. " created smoke puff!")
        end

        -- Press G for sparks
        if InputPressed("g", player) then
            local playerPos = GetPlayerTransform(player).pos

            table.insert(shared.particleEvents, {
                type = "sparks",
                position = playerPos,
                playerId = player
            })

            DebugPrint("Player " .. player .. " created sparks!")
        end
    end
end

function client.tick(dt)
    -- Client handles creating the actual particle effects

    -- Process particle events from server
    if shared.particleEvents then
        for i = 1, #shared.particleEvents do
            local event = shared.particleEvents[i]

            if event.type == "fire_explosion" then
                -- Create fire explosion particles
                for j = 1, 20 do  -- Spawn 20 fire particles
                    ParticleReset()
                    ParticleType("fire")
                    ParticleColor(1, 0.9, 0.2, 1, 0.8, 0.1)  -- Yellow to orange fade
                    ParticleAlpha(0.8, 0.0)  -- Fade out
                    ParticleRadius(0.1, 0.4)  -- Start small, grow bigger
                    ParticleEmissive(5, 1)  -- Bright glow that fades
                    ParticleGravity(-2)  -- Float upward slightly

                    -- Random direction for explosion effect
                    local randomDir = Vec(
                        (math.random() - 0.5) * 10,
                        math.random() * 5,
                        (math.random() - 0.5) * 10
                    )
                    SpawnParticle(event.position, randomDir, 1.5)  -- 1.5 second lifetime
                end

            elseif event.type == "smoke_puff" then
                -- Create smoke puff particles
                for j = 1, 15 do  -- Spawn 15 smoke particles
                    ParticleReset()
                    ParticleType("smoke")
                    ParticleColor(0.8, 0.8, 0.8, 0.4, 0.4, 0.4)  -- Light to dark gray
                    ParticleAlpha(0.6, 0.0)  -- Fade out
                    ParticleRadius(0.2, 0.8)  -- Grow larger
                    ParticleGravity(-1, -3)  -- Float upward
                    ParticleDrag(0.5)  -- Slow down over time

                    -- Random upward direction
                    local smokeDir = Vec(
                        (math.random() - 0.5) * 2,
                        math.random() * 3 + 1,  -- Always go up
                        (math.random() - 0.5) * 2
                    )
                    SpawnParticle(event.position, smokeDir, 3.0)  -- 3 second lifetime
                end

            elseif event.type == "sparks" then
                -- Create spark particles
                for j = 1, 25 do  -- Spawn 25 spark particles
                    ParticleReset()
                    ParticleType("fire")  -- Use fire type for sparks
                    ParticleColor(1, 1, 0.5, 1, 0.3, 0.1)  -- Bright yellow to dim red
                    ParticleAlpha(1.0, 0.0)  -- Bright fade to nothing
                    ParticleRadius(0.05, 0.02)  -- Small and shrinking
                    ParticleEmissive(8, 0)  -- Very bright, fade to nothing
                    ParticleGravity(5)  -- Fall down like real sparks

                    -- Random directions, mostly outward and up
                    local sparkDir = Vec(
                        (math.random() - 0.5) * 8,
                        math.random() * 6 + 2,  -- Mostly upward
                        (math.random() - 0.5) * 8
                    )
                    SpawnParticle(event.position, sparkDir, 0.8)  -- Quick 0.8s lifetime
                end
            end
        end

        -- Clear particle events after processing (only host clears)
        if GetLocalPlayer() == 1 then  -- Only host clears the events
            shared.particleEvents = {}
        end
    end
end
""",

"Trigger Zone Mod": """
-- Trigger Zone Multiplayer Mod Template
-- Shows how to detect when players enter and exit trigger areas

-- Trigger handles and player tracking
local triggerZones = {}
local playerInZone = {}  -- Track which players are in which zones

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Trigger zone mod server loaded!")

    -- Find all trigger zones in the scene
    triggerZones = {}

    -- Look for specifically named triggers
    local safeZone = FindTrigger("safe_zone")
    if safeZone ~= 0 then
        triggerZones["safe_zone"] = safeZone
        DebugPrint("Found safe zone trigger!")
    end

    local dangerZone = FindTrigger("danger_zone")
    if dangerZone ~= 0 then
        triggerZones["danger_zone"] = dangerZone
        DebugPrint("Found danger zone trigger!")
    end

    local goalZone = FindTrigger("goal")
    if goalZone ~= 0 then
        triggerZones["goal"] = goalZone
        DebugPrint("Found goal trigger!")
    end

    -- If no named triggers found, find any triggers
    if next(triggerZones) == nil then
        local allTriggers = FindTriggers("", true)  -- Find all triggers
        for i = 1, #allTriggers do
            triggerZones["zone_" .. i] = allTriggers[i]
        end
        DebugPrint("Found " .. #allTriggers .. " trigger zones")
    end

    -- Initialize player tracking
    playerInZone = {}

    -- Server state for clients
    shared.zoneEvents = {}
    shared.playersInZones = {}
end

function client.init()
    DebugPrint("Trigger zone mod client loaded!")
end

function server.tick(dt)
    -- Server handles trigger zone detection

    local players = GetAllPlayers()

    -- Initialize new players
    for i = 1, #players do
        local player = players[i]
        if not playerInZone[player] then
            playerInZone[player] = {}
        end
    end

    -- Check each player against each trigger zone
    for player = 1, #players do
        local playerPos = GetPlayerTransform(players[player]).pos

        for zoneName, trigger in pairs(triggerZones) do
            if IsHandleValid(trigger) then
                local isInZone = IsPointInTrigger(trigger, playerPos)
                local wasInZone = playerInZone[players[player]][zoneName] or false

                -- Player just entered zone
                if isInZone and not wasInZone then
                    playerInZone[players[player]][zoneName] = true

                    -- Add zone enter event
                    table.insert(shared.zoneEvents, {
                        type = "enter",
                        player = players[player],
                        zone = zoneName,
                        time = GetTime()
                    })

                    DebugPrint("Player " .. players[player] .. " entered " .. zoneName)

                    -- Special zone actions
                    if zoneName == "safe_zone" then
                        DebugPrint("Player " .. players[player] .. " is now safe!")
                    elseif zoneName == "danger_zone" then
                        DebugPrint("Player " .. players[player] .. " entered danger!")
                    elseif zoneName == "goal" then
                        DebugPrint("Player " .. players[player] .. " reached the goal!")
                        shared.winner = players[player]
                    end

                -- Player just left zone
                elseif not isInZone and wasInZone then
                    playerInZone[players[player]][zoneName] = false

                    -- Add zone exit event
                    table.insert(shared.zoneEvents, {
                        type = "exit",
                        player = players[player],
                        zone = zoneName,
                        time = GetTime()
                    })

                    DebugPrint("Player " .. players[player] .. " left " .. zoneName)

                    -- Special zone actions
                    if zoneName == "safe_zone" then
                        DebugPrint("Player " .. players[player] .. " left safety!")
                    elseif zoneName == "danger_zone" then
                        DebugPrint("Player " .. players[player] .. " escaped danger!")
                    end
                end
            end
        end
    end

    -- Sync current zone status to clients
    shared.playersInZones = {}
    for player = 1, #players do
        shared.playersInZones[players[player]] = playerInZone[players[player]] or {}
    end
end

function client.tick(dt)
    -- Client can react to zone events if needed
    -- Most zone logic happens on server
end

function client.draw()
    -- Show zone status and information
    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("Trigger Zone Status:")

        -- Show current zones for local player
        local localPlayer = GetLocalPlayer()
        if shared.playersInZones and shared.playersInZones[localPlayer] then
            UiTranslate(0, 30)

            local inAnyZone = false
            for zoneName, inZone in pairs(shared.playersInZones[localPlayer]) do
                if inZone then
                    inAnyZone = true

                    -- Color code different zone types
                    if zoneName == "safe_zone" then
                        UiColor(0, 1, 0)  -- Green for safe
                        UiText("✓ In Safe Zone")
                    elseif zoneName == "danger_zone" then
                        UiColor(1, 0, 0)  -- Red for danger
                        UiText("⚠ In Danger Zone")
                    elseif zoneName == "goal" then
                        UiColor(1, 1, 0)  -- Yellow for goal
                        UiText("★ At Goal!")
                    else
                        UiColor(0, 0.8, 1)  -- Blue for other zones
                        UiText("• In " .. zoneName)
                    end
                    UiTranslate(0, 20)
                end
            end

            if not inAnyZone then
                UiColor(0.7, 0.7, 0.7)
                UiText("Outside all zones")
            end
        else
            UiTranslate(0, 30)
            UiColor(0.5, 0.5, 0.5)
            UiText("No zone data")
        end

        -- Show winner if someone reached goal
        if shared.winner then
            UiTranslate(0, 50)
            UiColor(1, 1, 0)
            UiText("Winner: Player " .. shared.winner .. "!")
        end

    UiPop()
end
""",

"Custom Tool Mod": """
-- Custom Tool Multiplayer Mod Template
-- Shows how to register and implement a custom tool with ammo and effects

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Custom tool mod server loaded!")

    -- Register our custom tool
    RegisterTool("laser_gun", "Laser Gun", "MOD/vox/laser_gun.vox", 1)

    -- Set tool properties
    SetToolAmmoPickupAmount("laser_gun", 25)  -- Each ammo pickup gives 25 shots
    SetBool("game.tool.laser_gun.enabled", true)  -- Enable the tool

    -- Server tracks tool events
    shared.toolEvents = {}
    shared.totalShots = 0
end

function client.init()
    DebugPrint("Custom tool mod client loaded!")

    -- Load tool sound effects
    laserSound = LoadSound("MOD/sounds/laser_fire.ogg", 10.0)
    reloadSound = LoadSound("MOD/sounds/reload.ogg", 5.0)
end

function server.tick(dt)
    -- Server handles tool logic and player management

    -- Initialize new players with the tool
    local addedPlayers = GetAddedPlayers()
    for i = 1, #addedPlayers do
        local player = addedPlayers[i]

        -- Give player the custom tool and some ammo
        SetToolEnabled("laser_gun", true, player)
        SetToolAmmo("laser_gun", 50, player)  -- Start with 50 ammo

        DebugPrint("Player " .. player .. " received laser gun with 50 ammo!")
    end

    -- Check all players using the tool
    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]

        -- Check if player is using our custom tool
        if GetPlayerTool(player) == "laser_gun" then

            -- Player fires the tool (left mouse button)
            if InputDown("usetool", player) then
                local ammo = GetToolAmmo("laser_gun", player)

                if ammo > 0 then
                    -- Fire the laser
                    local camera = GetPlayerCameraTransform(player)
                    local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 100)

                    if hit then
                        local hitPos = VecAdd(camera.pos, VecScale(camera.fwd, dist))

                        -- Create explosion at hit location
                        Explosion(hitPos, 1.0)  -- Small explosion

                        -- Add tool fire event for effects
                        table.insert(shared.toolEvents, {
                            type = "laser_fire",
                            startPos = camera.pos,
                            endPos = hitPos,
                            playerId = player
                        })

                        shared.totalShots = (shared.totalShots or 0) + 1
                        DebugPrint("Player " .. player .. " fired laser! (Total shots: " .. shared.totalShots .. ")")
                    end

                    -- Use up ammo
                    SetToolAmmo("laser_gun", ammo - 1, player)

                    if ammo - 1 == 0 then
                        DebugPrint("Player " .. player .. " is out of ammo!")
                    end
                else
                    -- No ammo left - could play empty sound or show message
                    DebugPrint("Player " .. player .. " tried to fire but no ammo!")
                end
            end

            -- Player reloads the tool (R key)
            if InputPressed("r", player) then
                local currentAmmo = GetToolAmmo("laser_gun", player)
                if currentAmmo < 100 then  -- Max ammo is 100
                    SetToolAmmo("laser_gun", 100, player)  -- Full reload

                    -- Add reload event
                    table.insert(shared.toolEvents, {
                        type = "reload",
                        playerId = player
                    })

                    DebugPrint("Player " .. player .. " reloaded laser gun!")
                else
                    DebugPrint("Player " .. player .. " already has full ammo!")
                end
            end
        end
    end
end

function client.tick(dt)
    -- Client handles tool effects and feedback

    -- Process tool events from server
    if shared.toolEvents then
        for i = 1, #shared.toolEvents do
            local event = shared.toolEvents[i]

            if event.type == "laser_fire" then
                -- Play laser sound
                PlaySound(laserSound, event.startPos, 1.0)

                -- Create particle effects at hit point
                for j = 1, 10 do
                    ParticleReset()
                    ParticleType("fire")
                    ParticleColor(0, 1, 1, 0, 0.5, 1)  -- Cyan to blue
                    ParticleAlpha(1.0, 0.0)
                    ParticleRadius(0.05, 0.2)
                    ParticleEmissive(15, 0)  -- Bright glow

                    local randomDir = Vec(
                        (math.random() - 0.5) * 5,
                        (math.random() - 0.5) * 5,
                        (math.random() - 0.5) * 5
                    )
                    SpawnParticle(event.endPos, randomDir, 0.3)
                end

            elseif event.type == "reload" then
                -- Play reload sound
                PlaySound(reloadSound, GetPlayerTransform(event.playerId).pos, 0.8)
            end
        end

        -- Clear tool events after processing (only host clears)
        if GetLocalPlayer() == 1 then
            shared.toolEvents = {}
        end
    end
end

function client.draw()
    -- Show tool information and ammo count
    local localPlayer = GetLocalPlayer()

    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("Custom Laser Gun Tool:")

        UiTranslate(0, 30)

        -- Show if player has the tool equipped
        if GetPlayerTool(localPlayer) == "laser_gun" then
            local ammo = GetToolAmmo("laser_gun", localPlayer)

            -- Color code ammo display
            if ammo > 20 then
                UiColor(0, 1, 0)  -- Green for plenty of ammo
            elseif ammo > 5 then
                UiColor(1, 1, 0)  -- Yellow for low ammo
            else
                UiColor(1, 0, 0)  -- Red for very low ammo
            end

            UiText("Ammo: " .. ammo .. " / 100")

            UiTranslate(0, 20)
            UiColor(0.8, 0.8, 0.8)
            UiText("Hold LEFT CLICK to fire")

            UiTranslate(0, 20)
            UiText("Press R to reload")

        else
            UiColor(0.5, 0.5, 0.5)
            UiText("Equip Laser Gun to see ammo")
        end

        -- Show global stats
        UiTranslate(0, 50)
        UiColor(1, 1, 1)
        local totalShots = shared.totalShots or 0
        UiText("Total shots fired: " .. totalShots)

    UiPop()
end
""",

"Fire & Heat Mod": """
-- Fire & Heat Multiplayer Mod Template
-- Shows how to spawn fire, detect heat, and create fire-based gameplay

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Fire & heat mod server loaded!")

    -- Server tracks fire events and heat effects
    shared.fireEvents = {}
    shared.totalFires = 0
    shared.heatZones = {}  -- Track hot areas
end

function client.init()
    DebugPrint("Fire & heat mod client loaded!")

    -- Load fire-related sounds
    fireSound = LoadSound("MOD/sounds/fire_start.ogg", 8.0)
    extinguishSound = LoadSound("MOD/sounds/extinguish.ogg", 6.0)
end

function server.tick(dt)
    -- Server handles fire spawning and heat mechanics

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]
        local camera = GetPlayerCameraTransform(player)

        -- Press SPACE to spawn fire where player is looking
        if InputPressed("space", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local firePos = VecAdd(camera.pos, VecScale(camera.fwd, dist))
                SpawnFire(firePos)

                -- Add fire spawn event
                table.insert(shared.fireEvents, {
                    type = "fire_spawned",
                    position = firePos,
                    playerId = player
                })

                shared.totalFires = (shared.totalFires or 0) + 1
                DebugPrint("Player " .. player .. " started fire #" .. shared.totalFires)
            end
        end

        -- Press F to create fire spread (multiple fires in area)
        if InputPressed("f", player) then
            local hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)

            if hit then
                local centerPos = VecAdd(camera.pos, VecScale(camera.fwd, dist))

                -- Create multiple fires in a small area (fire spread effect)
                for j = 1, 5 do
                    local spreadPos = VecAdd(centerPos, Vec(
                        (math.random() - 0.5) * 4,  -- Random X offset
                        0,                          -- Keep Y same
                        (math.random() - 0.5) * 4   -- Random Z offset
                    ))
                    SpawnFire(spreadPos)
                end

                table.insert(shared.fireEvents, {
                    type = "fire_spread",
                    position = centerPos,
                    playerId = player
                })

                DebugPrint("Player " .. player .. " created fire spread!")
            end
        end

        -- Press E to extinguish nearby fires
        if InputPressed("e", player) then
            local playerPos = GetPlayerTransform(player).pos
            local extinguished = 0

            -- Check all active fires
            local fireCount = GetFireCount()
            for fireIndex = 1, fireCount do
                local firePos, fireSize = GetFireInfo(fireIndex)
                if firePos then
                    local distance = VecLength(VecSub(playerPos, firePos))

                    if distance < 5.0 then  -- Within 5 meters
                        RemoveFire(fireIndex)
                        extinguished = extinguished + 1

                        -- Add extinguish event
                        table.insert(shared.fireEvents, {
                            type = "fire_extinguished",
                            position = firePos,
                            playerId = player
                        })
                    end
                end
            end

            if extinguished > 0 then
                DebugPrint("Player " .. player .. " extinguished " .. extinguished .. " fires!")
            else
                DebugPrint("Player " .. player .. " - no fires nearby to extinguish")
            end
        end

        -- Press G to get heat information at player location
        if InputPressed("g", player) then
            local playerPos = GetPlayerTransform(player).pos
            local heatLevel = calculateHeatLevel(playerPos)

            table.insert(shared.fireEvents, {
                type = "heat_check",
                position = playerPos,
                heatLevel = heatLevel,
                playerId = player
            })

            DebugPrint("Player " .. player .. " heat level: " .. heatLevel)
        end
    end

    -- Update heat zones around active fires
    updateHeatZones()
end

-- Function to calculate heat level at a position
function calculateHeatLevel(pos)
    local totalHeat = 0
    local fireCount = GetFireCount()

    for i = 1, fireCount do
        local firePos, fireSize = GetFireInfo(i)
        if firePos then
            local distance = VecLength(VecSub(pos, firePos))
            local maxHeatDistance = 8.0  -- Heat affects up to 8 meters

            if distance < maxHeatDistance then
                -- Heat decreases with distance
                local heatContribution = (fireSize or 1) * (1 - distance / maxHeatDistance)
                totalHeat = totalHeat + heatContribution
            end
        end
    end

    return math.floor(totalHeat * 100)  -- Return as percentage (0-100+)
end

-- Function to update heat zones for client sync
function updateHeatZones()
    shared.heatZones = {}
    local fireCount = GetFireCount()

    for i = 1, fireCount do
        local firePos, fireSize = GetFireInfo(i)
        if firePos then
            table.insert(shared.heatZones, {
                position = firePos,
                size = fireSize or 1,
                heatRadius = 8.0
            })
        end
    end

    shared.activeFireCount = fireCount
end

function client.tick(dt)
    -- Client handles fire effects and feedback

    -- Process fire events from server
    if shared.fireEvents then
        for i = 1, #shared.fireEvents do
            local event = shared.fireEvents[i]

            if event.type == "fire_spawned" or event.type == "fire_spread" then
                -- Play fire sound
                PlaySound(fireSound, event.position, 0.8)

                -- Create fire particles
                for j = 1, 15 do
                    ParticleReset()
                    ParticleType("fire")
                    ParticleColor(1, 0.8, 0.2, 1, 0.3, 0.1)  -- Orange to red
                    ParticleAlpha(0.8, 0.0)
                    ParticleRadius(0.1, 0.3)
                    ParticleEmissive(8, 1)
                    ParticleGravity(-3, -5)  -- Float upward

                    local fireDir = Vec(
                        (math.random() - 0.5) * 2,
                        math.random() * 4 + 1,
                        (math.random() - 0.5) * 2
                    )
                    SpawnParticle(event.position, fireDir, 2.0)
                end

            elseif event.type == "fire_extinguished" then
                -- Play extinguish sound
                PlaySound(extinguishSound, event.position, 0.6)

                -- Create steam/smoke particles
                for j = 1, 10 do
                    ParticleReset()
                    ParticleType("smoke")
                    ParticleColor(0.9, 0.9, 0.9, 0.5, 0.5, 0.5)
                    ParticleAlpha(0.7, 0.0)
                    ParticleRadius(0.2, 0.6)
                    ParticleGravity(-2)

                    local smokeDir = Vec(
                        (math.random() - 0.5) * 3,
                        math.random() * 3 + 2,
                        (math.random() - 0.5) * 3
                    )
                    SpawnParticle(event.position, smokeDir, 1.5)
                end
            end
        end

        -- Clear fire events after processing
        if GetLocalPlayer() == 1 then
            shared.fireEvents = {}
        end
    end
end

function client.draw()
    -- Show fire and heat information
    local localPlayer = GetLocalPlayer()

    UiPush()
        UiTranslate(50, 50)
        UiColor(1, 1, 1)
        UiText("Fire & Heat System:")

        UiTranslate(0, 30)
        local fireCount = shared.activeFireCount or 0

        -- Color code fire count
        if fireCount > 10 then
            UiColor(1, 0, 0)  -- Red for many fires
        elseif fireCount > 5 then
            UiColor(1, 0.5, 0)  -- Orange for some fires
        elseif fireCount > 0 then
            UiColor(1, 1, 0)  -- Yellow for few fires
        else
            UiColor(0, 1, 0)  -- Green for no fires
        end
        UiText("Active fires: " .. fireCount)

        -- Show heat level at player position
        UiTranslate(0, 25)
        local playerPos = GetPlayerTransform(localPlayer).pos
        local heatLevel = 0

        -- Calculate heat level for local display
        if shared.heatZones then
            for i = 1, #shared.heatZones do
                local zone = shared.heatZones[i]
                local distance = VecLength(VecSub(playerPos, zone.position))
                if distance < zone.heatRadius then
                    local contribution = zone.size * (1 - distance / zone.heatRadius)
                    heatLevel = heatLevel + contribution
                end
            end
        end

        heatLevel = math.floor(heatLevel * 100)

        -- Color code heat level
        if heatLevel > 80 then
            UiColor(1, 0, 0)    -- Red for extreme heat
            UiText("🔥 Heat: " .. heatLevel .. "% (EXTREME)")
        elseif heatLevel > 40 then
            UiColor(1, 0.5, 0)  -- Orange for high heat
            UiText("🔥 Heat: " .. heatLevel .. "% (HIGH)")
        elseif heatLevel > 10 then
            UiColor(1, 1, 0)    -- Yellow for warm
            UiText("🔥 Heat: " .. heatLevel .. "% (WARM)")
        else
            UiColor(0.7, 0.7, 0.7)  -- Gray for cool
            UiText("❄️ Heat: " .. heatLevel .. "% (COOL)")
        end

        -- Show controls
        UiTranslate(0, 40)
        UiColor(0.8, 0.8, 0.8)
        UiText("SPACE - Spawn fire")

        UiTranslate(0, 18)
        UiText("F - Fire spread")

        UiTranslate(0, 18)
        UiText("E - Extinguish nearby fires")

        UiTranslate(0, 18)
        UiText("G - Check heat level")

        -- Show total fires spawned
        UiTranslate(0, 30)
        UiColor(1, 1, 1)
        local totalFires = shared.totalFires or 0
        UiText("Total fires spawned: " .. totalFires)

    UiPop()
end
""",

"Sound & Music Mod": """
-- Sound and Music Multiplayer Mod Template
-- Shows how to load and play sounds, music, and sound loops

-- Sound handles (loaded once on each client)
local buttonSound = nil
local ambientLoop = nil
local explosionSound = nil

function shared.init()
    -- Shared initialization
end

function server.init()
    DebugPrint("Sound mod server loaded!")

    -- Server tracks sound events to sync to clients
    shared.soundEvents = {}
    shared.musicPlaying = false
    shared.soundCount = 0
end

function client.init()
    DebugPrint("Sound mod client loaded!")

    -- Load sounds on each client (sounds are client-side resources)
    buttonSound = LoadSound("MOD/sounds/button_click.ogg")
    explosionSound = LoadSound("MOD/sounds/explosion.ogg", 15.0)  -- 15m nominal distance

    -- Load ambient loop
    ambientLoop = LoadLoop("MOD/sounds/ambient_forest.ogg", 20.0)

    -- Start background music
    PlayMusic("MOD/music/background.ogg")
end

function server.tick(dt)
    -- Server handles game logic and triggers sound events

    local players = GetAllPlayers()
    for i = 1, #players do
        local player = players[i]

        -- Press SPACE for explosion sound at player location
        if InputPressed("space", player) then
            local playerPos = GetPlayerTransform(player).pos

            -- Add sound event to shared table for clients to play
            table.insert(shared.soundEvents, {
                type = "explosion",
                position = playerPos,
                playerId = player,
                volume = 1.0
            })

            shared.soundCount = (shared.soundCount or 0) + 1
            DebugPrint("Player " .. player .. " triggered explosion sound!")
        end

        -- Press T to toggle music
        if InputPressed("t", player) then
            shared.musicPlaying = not shared.musicPlaying
            shared.soundEvents[#shared.soundEvents + 1] = {
                type = "music_toggle",
                enable = shared.musicPlaying
            }
            DebugPrint("Player " .. player .. " toggled music: " .. (shared.musicPlaying and "ON" or "OFF"))
        end

        -- Press F for UI button sound (no position needed)
        if InputPressed("f", player) then
            shared.soundEvents[#shared.soundEvents + 1] = {
                type = "ui_button",
                playerId = player
            }
            DebugPrint("Player " .. player .. " triggered UI sound!")
        end
    end
end

function client.tick(dt)
    -- Client handles playing the actual sounds

    -- Play ambient loop continuously at world center
    local loopPos = Vec(0, 5, 0)
    PlayLoop(ambientLoop, loopPos, 0.3)  -- Quiet ambient volume

    -- Process sound events from server
    if shared.soundEvents then
        for i = 1, #shared.soundEvents do
            local event = shared.soundEvents[i]

            if event.type == "explosion" then
                -- Play positioned explosion sound
                PlaySound(explosionSound, event.position, event.volume)

            elseif event.type == "music_toggle" then
                -- Toggle background music
                if event.enable then
                    if not IsMusicPlaying() then
                        PlayMusic("MOD/music/background.ogg")
                    end
                else
                    StopMusic()
                end

            elseif event.type == "ui_button" then
                -- Play UI sound (no position - plays at player location)
                UiSound("MOD/sounds/button_click.ogg", 0.5)  -- Volume 0.5
            end
        end

        -- Clear sound events after processing (only on local client)
        if GetLocalPlayer() == 1 then  -- Only host clears the events
            shared.soundEvents = {}
        end
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