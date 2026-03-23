# Teardown API Function Definitions
# This file contains all the user-friendly function definitions for the GUI

TEARDOWN_FUNCTIONS = {


    #core functions
    "Server Setup": {
        "category": "Core Functions",
        "code": "function server.init()\n    -- Your setup code here\nend",
        "description": "Runs once when the script starts on the server"
    },
    "Client Setup": {
        "category": "Core Functions", 
        "code": "function client.init()\n    -- Your client setup code here\nend",
        "description": "Runs once when the script starts on each client"
    },
    "Always Run (Server)": {
        "category": "Core Functions",
        "code": "function server.tick(dt)\n    -- Code that runs every frame on server\nend",
        "description": "Runs every frame on the server. dt = time since last frame"
    },
    "Fixed Update (Server)": {
        "category": "Core Functions",
        "code": "function server.update(dt)\n    -- Fixed 60fps update rate\nend",
        "description": "Called at fixed 60fps rate, may not run every frame"
    },
    "Post-Physics Update (Server)": {
        "category": "Core Functions",
        "code": "function server.postUpdate(dt)\n    -- After physics calculations\nend",
        "description": "Called after physics, for additional calculations"
    },
    "Destroy Script (Server)": {
        "category": "Core Functions",
        "code": "function server.destroy()\n    -- Cleanup when game mode stops\nend",
        "description": "Called when game mode is stopped (cleanup)"
    },
    "Always Run (Client)": {
        "category": "Core Functions",
        "code": "function client.tick(dt)\n    -- Code that runs every frame on client\nend", 
        "description": "Runs every frame on each client. dt = time since last frame"
    },
    "Fixed Update (Client)": {
        "category": "Core Functions",
        "code": "function client.update(dt)\n    -- Fixed 60fps update rate\nend",
        "description": "Called at fixed 60fps rate, may not run every frame"
    },
    "Post-Physics Update (Client)": {
        "category": "Core Functions",
        "code": "function client.postUpdate(dt)\n    -- After physics calculations\nend",
        "description": "Called after physics, for animations and effects"
    },
    "Draw UI (Client)": {
        "category": "Core Functions",
        "code": "function client.draw()\n    -- UI drawing code here\nend",
        "description": "Draw 2D overlay, after scene but before HUD"
    },
    "Render Scene (Client)": {
        "category": "Core Functions",
        "code": "function client.render(dt)\n    -- Before drawing to screen\nend",
        "description": "Called right before objects are drawn to screen"
    },
    "Destroy Script (Client)": {
        "category": "Core Functions",
        "code": "function client.destroy()\n    -- Cleanup when game mode stops\nend",
        "description": "Called when game mode is stopped (cleanup)"
    },


    #objects
    "Find an Object": {
        "category": "Objects",
        "code": 'local object = FindEntity("my_object")',
        "description": "Find an object by its name in the scene"
    },
    "Find All Objects": {
        "category": "Objects",
        "code": 'local objects = FindEntities("type")',
        "description": "Find all objects of a certain type"
    },
    "Get Object's Children": {
        "category": "Objects",
        "code": "local children = GetEntityChildren(object)",
        "description": "Get all child objects of an object"
    },
    "Get Object's Parent": {
        "category": "Objects",
        "code": "local parent = GetEntityParent(object)",
        "description": "Get the parent object of an object"
    },
    "Add a Tag to an Object": {
        "category": "Objects",
        "code": 'SetTag(object, "custom_tag", "value")',
        "description": "Add a custom tag to an object"
    },
    "Remove a Tag from Object": {
        "category": "Objects",
        "code": 'RemoveTag(object, "custom_tag")',
        "description": "Remove a tag from an object"
    },
    "Check if an Object has a Tag": {
        "category": "Objects",
        "code": 'if HasTag(object, "explosive") then\n    -- Object is explosive\nend',
        "description": "Check if an object has a specific tag"
    },
    "Get Tag Value": {
        "category": "Objects",
        "code": "local value = GetTagValue(object, \"tag_name\")",
        "description": "Get the value associated with a tag"
    },
    "List All Tags": {
        "category": "Objects",
        "code": "local tags = ListTags(object)",
        "description": "Get all tags on an object"
    },
    "Get Object Description": {
        "category": "Objects",
        "code": "local desc = GetDescription(object)",
        "description": "Get the description text of an object"
    },
    "Set Object Description": {
        "category": "Objects",
        "code": 'SetDescription(object, "Custom description")',
        "description": "Set the description text of an object (shows on HUD)"
    },
    "Delete an Object": {
        "category": "Objects",
        "code": "Delete(object)",
        "description": "Remove an object from the scene"
    },
    "Check if Object Exists": {
        "category": "Objects",
        "code": "if IsHandleValid(object) then\n    -- Object still exists\nend",
        "description": "Check if an object handle is still valid"
    },
    "Get Object Type": {
        "category": "Objects",
        "code": "local type = GetEntityType(object)",
        "description": "Get the type of an object (body, shape, light, etc.)"
    },
    "Get Object Property": {
        "category": "Objects",
        "code": "local value = GetProperty(object, \"property_name\")",
        "description": "Get a property value from an object"
    },
    "Set Object Property": {
        "category": "Objects",
        "code": "SetProperty(object, \"property_name\", value)",
        "description": "Set a property value on an object (server only)"
    },
    "Find a Location Marker": {
        "category": "Objects",
        "code": 'local location = FindLocation("location_name")',
        "description": "Find a location marker placed in editor"
    },
    "Find All Location Markers": {
        "category": "Objects",
        "code": 'local locations = FindLocations("location_name")',
        "description": "Find all location markers with a specific tag"
    },
    "Get a Location Marker Position": {
        "category": "Objects",
        "code": "local transform = GetLocationTransform(location)",
        "description": "Get the world position and rotation of a location marker"
    },
    "Get Material at Position": {
        "category": "Objects",
        "code": "local material = GetShapeMaterialAtPosition(shape, position)",
        "description": "Get the material at a specific position on a shape"
    },
    "Get Material by Index": {
        "category": "Objects",
        "code": "local material = GetShapeMaterialAtIndex(shape, index)",
        "description": "Get the material at a specific voxel index"
    },
    "Get Material Properties": {
        "category": "Objects",
        "code": "local material = GetShapeMaterial(shape, material_index)",
        "description": "Get properties of a specific material"
    },
    "Set Drawing Brush": {
        "category": "Objects",
        "code": "SetBrush(brush_settings)",
        "description": "Set the material for drawing operations"
    },
    

    #physics
    "Push an Object": {
        "category": "Physics",
        "code": 'ApplyBodyImpulse(body, position, direction * force)',
        "description": "Apply a push/impulse force to an object"
    },
    "Set an Object's Speed": {
        "category": "Physics",
        "code": 'SetBodyVelocity(body, velocity_vector)',
        "description": "Set the velocity of an object"
    },
    "Make an Object Move": {
        "category": "Physics",
        "code": 'SetBodyDynamic(body, true)',
        "description": "Make an object affected by physics"
    },


    #events
    "Listen for Player Damage": {
        "category": "Events",
        "code": 'function playerhurt(playerId, healthBefore, healthAfter, attackerId, point, impulse)\n    -- Player was hurt\nend',
        "description": "This function runs when any player gets hurt"
    },
    "Make an Explosion": {
        "category": "Events",
        "code": 'function explosion(point, strength)\n    -- Explosion occurred\nend',
        "description": "This function runs when an explosion happens"
    },
    "Send a Custom Event": {
        "category": "Events",
        "code": 'PostEvent("my_custom_event", data)',
        "description": "Send a custom event that other scripts can listen for"
    },
    "Get Event Count": {
        "category": "Events",
        "code": "local count = GetEventCount(\"event_type\")",
        "description": "Get how many events of a certain type are available"
    },
    "Get Event Data": {
        "category": "Events",
        "code": "local event_data = GetEvent(\"event_type\", index)",
        "description": "Get specific event data by type and index"
    },
    "Register Event Listener": {
        "category": "Events",
        "code": 'RegisterListenerTo("event_name", "function_name")',
        "description": "Bind function to event (deprecated)"
    },
    "Unregister Event Listener": {
        "category": "Events",
        "code": 'UnregisterListener("event_name", "function_name")',
        "description": "Remove event listener (deprecated)"
    },
    "Trigger Legacy Event": {
        "category": "Events",
        "code": 'TriggerEvent("event_name", "arguments")',
        "description": "Trigger old-style event (deprecated)"
    },


    #lighting
    "Find a Light": {
        "category": "Lighting",
        "code": 'local light = FindLight("light_name")',
        "description": "Find a light source in the scene"
    },
    "Find All Lights": {
        "category": "Lighting",
        "code": 'local lights = FindLights("light_name")',
        "description": "Find all light sources with a specific tag"
    },
    "Turn a Light On/Off": {
        "category": "Lighting",
        "code": "SetLightEnabled(light, true)",
        "description": "Enable or disable a light source"
    },
    "Change a Light's Color": {
        "category": "Lighting",
        "code": "SetLightColor(light, color)",
        "description": "Change the color of a light source"
    },
    "Change a Light's Brightness": {
        "category": "Lighting",
        "code": "SetLightIntensity(light, intensity)",
        "description": "Change the brightness of a light source"
    },
    "Get Light's Position": {
        "category": "Lighting",
        "code": "local transform = GetLightTransform(light)",
        "description": "Get the world position of a light"
    },
    "Get Light's Shape": {
        "category": "Lighting",
        "code": "local shape = GetLightShape(light)",
        "description": "Get the shape that owns this light"
    },
    "Check if Light is Active": {
        "category": "Lighting",
        "code": "if IsLightActive(light) then\n    -- Light is currently on\nend",
        "description": "Check if a light is currently active"
    },
    "Check if Point is Lit": {
        "category": "Lighting",
        "code": "if IsPointAffectedByLight(light, position) then\n    -- Point is illuminated\nend",
        "description": "Check if a position is affected by a light"
    },
    "Get Player's Flashlight": {
        "category": "Lighting",
        "code": "local flashlight = GetFlashlight()",
        "description": "Get the player's flashlight"
    },
    "Set Player's Flashlight": {
        "category": "Lighting",
        "code": "SetFlashlight(flashlight)",
        "description": "Set the player's flashlight"
    },
    
    #triggers
    "Check if an Object is in a Trigger": {
        "category": "Triggers",
        "code": "if IsBodyInTrigger(trigger, body) then\n    -- Object is in trigger\nend",
        "description": "Check if an object is inside a trigger area"
    },
    "Find a Trigger": {
        "category": "Triggers",
        "code": 'local trigger = FindTrigger("trigger_name")',
        "description": "Find a trigger area by its tag name"
    },
    "Find All Triggers": {
        "category": "Triggers",
        "code": 'local triggers = FindTriggers("trigger_name")',
        "description": "Find all trigger areas with a specific tag"
    },
    "Get Trigger's Position": {
        "category": "Triggers",
        "code": "local transform = GetTriggerTransform(trigger)",
        "description": "Get the world position of a trigger"
    },
    "Set Trigger's Position": {
        "category": "Triggers",
        "code": "SetTriggerTransform(trigger, transform)",
        "description": "Set the world position of a trigger"
    },
    "Get Trigger's Bounds": {
        "category": "Triggers",
        "code": "local min, max = GetTriggerBounds(trigger)",
        "description": "Get the bounding box of a trigger"
    },
    "Check if Vehicle is in Trigger": {
        "category": "Triggers",
        "code": "if IsVehicleInTrigger(trigger, vehicle) then\n    -- Vehicle is in trigger\nend",
        "description": "Check if a vehicle is inside a trigger area"
    },
    "Check if Shape is in Trigger": {
        "category": "Triggers",
        "code": "if IsShapeInTrigger(trigger, shape) then\n    -- Shape is in trigger\nend",
        "description": "Check if a shape is inside a trigger area"
    },
    "Check if Point is in a Trigger": {
        "category": "Triggers",
        "code": "if IsPointInTrigger(trigger, point) then\n    -- Point is in trigger\nend",
        "description": "Check if a position is inside a trigger area"
    },
    "Check if Point is in Boundaries": {
        "category": "Triggers",
        "code": "if IsPointInBoundaries(trigger, point) then\n    -- Point is within boundaries\nend",
        "description": "Check if a point is within trigger boundaries"
    },
    "Check if Trigger is Empty": {
        "category": "Triggers",
        "code": "if IsTriggerEmpty(trigger) then\n    -- Trigger contains no objects\nend",
        "description": "Check if a trigger area is empty"
    },
    "Get Distance to Trigger": {
        "category": "Triggers",
        "code": "local distance = GetTriggerDistance(trigger, position)",
        "description": "Get distance from a point to the nearest trigger edge"
    },
    "Get Closest Point in Trigger": {
        "category": "Triggers",
        "code": "local point = GetTriggerClosestPoint(trigger, position)",
        "description": "Get the closest point inside a trigger to a position"
    },


    #players
    "Get You": {
        "category": "Players",
        "code": "local players = GetAllPlayers()",
        "description": "Get a list of all players in the game"
    },
    "Get Me": {
        "category": "Players",
        "code": "local player = GetLocalPlayer()",
        "description": "Get the local player (you)"
    },
    "Get a Player's Position": {
        "category": "Players",
        "code": "local pos = GetPlayerPos(player)",
        "description": "Get the position of a player"
    },
    "Set a Player's Health": {
        "category": "Players",
        "code": "SetPlayerHealth(player, health)",
        "description": "Set a player's health"
    },
    "Get a Player's Health": {
        "category": "Players",
        "code": "local health = GetPlayerHealth(player)",
        "description": "Get a player's current health"
    },
    "Respawn a Player": {
        "category": "Players",
        "code": "RespawnPlayer(player)",
        "description": "Respawn a player at their spawn point"
    },
    "Set a Player's Speed": {
        "category": "Players",
        "code": "SetPlayerWalkingSpeed(player, speed)",
        "description": "Change how fast a player can walk"
    },
    "Give a Player a Tool": {
        "category": "Players",
        "code": 'SetPlayerTool(player, "tool_name")',
        "description": "Give a player a specific tool"
    },
    "Get a Player's Tool": {
        "category": "Players",
        "code": "local tool = GetPlayerTool(player)",
        "description": "Get the current tool a player is holding"
    },
    "Hurt a Player": {
        "category": "Players",
        "code": "ApplyPlayerDamage(player, damage)",
        "description": "Apply damage to a player"
    },
    "Get Max Players": {
        "category": "Players",
        "code": "local max = GetMaxPlayers()",
        "description": "Get the maximum number of players allowed"
    },
    "Get Current Player Count": {
        "category": "Players",
        "code": "local count = GetPlayerCount()",
        "description": "Get how many players are currently in the game"
    },
    "Get New Players": {
        "category": "Players",
        "code": "local new_players = GetAddedPlayers()",
        "description": "Get players who joined since last update"
    },
    "Get Left Players": {
        "category": "Players",
        "code": "local left_players = GetRemovedPlayers()",
        "description": "Get players who left since last update"
    },
    "Get Player's Name": {
        "category": "Players",
        "code": "local name = GetPlayerName(player)",
        "description": "Get the display name of a player"
    },
    "Check if Player is Local": {
        "category": "Players",
        "code": "if IsPlayerLocal(player) then\n    -- This is the local player\nend",
        "description": "Check if a player is the local client"
    },
    "Get Player's Character": {
        "category": "Players",
        "code": "local character = GetPlayerCharacter(player)",
        "description": "Get the character type a player is using"
    },
    "Check if Player is Host": {
        "category": "Players",
        "code": "if IsPlayerHost(player) then\n    -- This player is the host\nend",
        "description": "Check if a player is the game host"
    },
    "Check if Player is Valid": {
        "category": "Players",
        "code": "if IsPlayerValid(player) then\n    -- Player is active\nend",
        "description": "Check if a player ID is still valid"
    },
    "Get Player's Aim Info": {
        "category": "Players",
        "code": "local hit, point, normal, shape, body, dist, t, material = GetPlayerAimInfo(position, max_distance)",
        "description": "Trace player's aim and get hit information"
    },
    "Get Player's Camera Pitch": {
        "category": "Players",
        "code": "local pitch = GetPlayerPitch(player)",
        "description": "Get how far up/down player is looking"
    },
    "Get Player's Camera Yaw": {
        "category": "Players",
        "code": "local yaw = GetPlayerYaw(player)",
        "description": "Get player's horizontal rotation angle"
    },
    "Set Player's Camera Pitch": {
        "category": "Players",
        "code": "SetPlayerPitch(angle, player)",
        "description": "Set how far up/down player looks (server only)"
    },
    "Get Player's Crouch Level": {
        "category": "Players",
        "code": "local crouch = GetPlayerCrouch(player)",
        "description": "Get how much a player is crouching"
    },
    "Get Player's Transform": {
        "category": "Players",
        "code": "local transform = GetPlayerTransform(player)",
        "description": "Get player's position and rotation (no pitch)"
    },
    "Get Player's Transform with Pitch": {
        "category": "Players",
        "code": "local transform = GetPlayerTransformWithPitch(player)",
        "description": "Get player's position and rotation (with pitch)"
    },
    "Teleport Player": {
        "category": "Players",
        "code": "SetPlayerTransform(transform, player)",
        "description": "Teleport player to position (server only)"
    },
    "Teleport Player with Pitch": {
        "category": "Players",
        "code": "SetPlayerTransformWithPitch(transform, player)",
        "description": "Teleport player preserving camera angle (server only)"
    },
    "Push Player on Ground": {
        "category": "Players",
        "code": "SetPlayerGroundVelocity(velocity, player)",
        "description": "Push player while on ground (conveyor effect)"
    },
    "Get Player's Eye Position": {
        "category": "Players",
        "code": "local transform = GetPlayerEyeTransform(player)",
        "description": "Get player's eye/camera position"
    },
    "Get Player's Camera": {
        "category": "Players",
        "code": "local transform = GetPlayerCameraTransform(player)",
        "description": "Get player's standard camera transform"
    },
    "Offset Player's Camera": {
        "category": "Players",
        "code": "SetPlayerCameraOffsetTransform(offset, true, player)",
        "description": "Apply camera offset (client only)"
    },
    "Set Player's Spawn Point": {
        "category": "Players",
        "code": "SetPlayerSpawnTransform(transform, player)",
        "description": "Set where player spawns (server only)"
    },
    "Set Player's Spawn Health": {
        "category": "Players",
        "code": "SetPlayerSpawnHealth(health, player)",
        "description": "Set player's health when spawning (server only)"
    },
    "Set Player's Spawn Tool": {
        "category": "Players",
        "code": 'SetPlayerSpawnTool("tool_name", player)',
        "description": "Set tool player spawns with (server only)"
    },
    "Get Player's Velocity": {
        "category": "Players",
        "code": "local velocity = GetPlayerVelocity(player)",
        "description": "Get how fast player is moving"
    },
    "Set Player's Velocity": {
        "category": "Players",
        "code": "SetPlayerVelocity(velocity, player)",
        "description": "Set player's movement speed (server only)"
    },
    "Get Player's Vehicle": {
        "category": "Players",
        "code": "local vehicle = GetPlayerVehicle(player)",
        "description": "Get vehicle player is in"
    },
    "Put Player in Vehicle": {
        "category": "Players",
        "code": "SetPlayerVehicle(vehicle, player)",
        "description": "Force player to enter/exit vehicle (server only)"
    },
    "Check if Player is on Ground": {
        "category": "Players",
        "code": "if IsPlayerGrounded(player) then\n    -- Player is touching ground\nend",
        "description": "Check if player's feet are on the ground"
    },
    "Check if Player is Driving": {
        "category": "Players",
        "code": "if IsPlayerVehicleDriver(vehicle, player) then\n    -- Player is driving\nend",
        "description": "Check if player is driving a vehicle"
    },
    "Check if Player is Passenger": {
        "category": "Players",
        "code": "if IsPlayerVehiclePassenger(vehicle, player) then\n    -- Player is passenger\nend",
        "description": "Check if player is passenger in vehicle"
    },
    "Check if Player is Jumping": {
        "category": "Players",
        "code": "if IsPlayerJumping(player) then\n    -- Player is jumping\nend",
        "description": "Check if player is currently jumping"
    },
    "Check if Player is Valid": {
        "category": "Players",
        "code": "if IsPlayerValid(player) then\n    -- Player exists and is valid\nend",
        "description": "Check if a player ID is valid (player exists)"
    },
    "Check if Player is Host": {
        "category": "Players",
        "code": "if IsPlayerHost(player) then\n    -- Player is the server host\nend",
        "description": "Check if player is the server host"
    },
    "Check if Player is Local": {
        "category": "Players",
        "code": "if IsPlayerLocal(player) then\n    -- Player is the local client\nend",
        "description": "Check if player is the local client (not remote)"
    },
    "Get Player's Ground Contact": {
        "category": "Players",
        "code": "local touching, shape, point, normal = GetPlayerGroundContact(player)",
        "description": "Get information about what player is standing on"
    },
    "Get Player's Grabbed Shape": {
        "category": "Players",
        "code": "local shape = GetPlayerGrabShape(player)",
        "description": "Get shape player is holding"
    },
    "Get Player's Grabbed Body": {
        "category": "Players",
        "code": "local body = GetPlayerGrabBody(player)",
        "description": "Get body player is holding"
    },
    "Make Player Release": {
        "category": "Players",
        "code": "ReleasePlayerGrab(player)",
        "description": "Force player to let go of grabbed object (server only)"
    },
    "Get Player's Grab Point": {
        "category": "Players",
        "code": "local point = GetPlayerGrabPoint(player)",
        "description": "Get where player is grabbing an object"
    },
    "Get Player's Focused Shape": {
        "category": "Players",
        "code": "local shape = GetPlayerPickShape(player)",
        "description": "Get shape under player's crosshair"
    },
    "Get Player's Focused Body": {
        "category": "Players",
        "code": "local body = GetPlayerPickBody(player)",
        "description": "Get body under player's crosshair"
    },
    "Get Player's Interactable Shape": {
        "category": "Players",
        "code": "local shape = GetPlayerInteractShape(player)",
        "description": "Get shape player can interact with"
    },
    "Get Player's Interactable Body": {
        "category": "Players",
        "code": "local body = GetPlayerInteractBody(player)",
        "description": "Get body player can interact with"
    },
    "Set Player's UI Screen": {
        "category": "Players",
        "code": "SetPlayerScreen(screen, player)",
        "description": "Assign UI screen for player to use (server only)"
    },
    "Get Player's UI Screen": {
        "category": "Players",
        "code": "local screen = GetPlayerScreen(player)",
        "description": "Get UI screen player is using"
    },
    "Check if Player Can Use Tools": {
        "category": "Players",
        "code": "if GetPlayerCanUseTool(player) then\n    -- Player can use tools\nend",
        "description": "Check if player can currently use tools"
    },
    "Set Player Health Regeneration": {
        "category": "Players",
        "code": "SetPlayerRegenerationState(true, player)",
        "description": "Enable/disable health regeneration (server only)"
    },
    "Respawn Player at Position": {
        "category": "Players",
        "code": "RespawnPlayerAtTransform(transform, player)",
        "description": "Respawn player at specific position (server only)"
    },
    "Get Player's Crouch Speed": {
        "category": "Players",
        "code": "local speed = GetPlayerCrouchSpeedScale(player)",
        "description": "Get player's speed multiplier while crouching"
    },
    "Set Player's Crouch Speed": {
        "category": "Players",
        "code": "SetPlayerCrouchSpeedScale(speed, player)",
        "description": "Set player's speed while crouching (server only)"
    },
    "Get Player's Hurt Speed": {
        "category": "Players",
        "code": "local speed = GetPlayerHurtSpeedScale(player)",
        "description": "Get player's speed penalty while hurt"
    },
    "Set Player's Hurt Speed": {
        "category": "Players",
        "code": "SetPlayerHurtSpeedScale(speed, player)",
        "description": "Set player's hurt speed penalty (server only)"
    },
    "Get Player Parameter": {
        "category": "Players",
        "code": "local value = GetPlayerParam(\"parameter_name\", player)",
        "description": "Get a player-specific parameter value"
    },
    "Set Player Parameter": {
        "category": "Players",
        "code": "SetPlayerParam(\"parameter_name\", value, player)",
        "description": "Set a player-specific parameter (server only)"
    },
    "Hide Player": {
        "category": "Players",
        "code": "SetPlayerHidden(player)",
        "description": "Hide player character model"
    },
    "Get Player's Color": {
        "category": "Players",
        "code": "local enabled, r, g, b = GetPlayerColor(player)",
        "description": "Get player's custom color settings"
    },
    "Set Player's Color": {
        "category": "Players",
        "code": "SetPlayerColor(r, g, b, player)",
        "description": "Change player's color"
    },
    "Disable Player Input": {
        "category": "Players",
        "code": "DisablePlayerInput(player)",
        "description": "Disable player's input (server only)"
    },
    "Disable Player Completely": {
        "category": "Players",
        "code": "DisablePlayer(player)",
        "description": "Disable player entirely (server only)"
    },
    "Check if Player is Disabled": {
        "category": "Players",
        "code": "if IsPlayerDisabled(player) then\n    -- Player is disabled\nend",
        "description": "Check if player has been disabled"
    },
    "Disable Player Damage": {
        "category": "Players",
        "code": "DisablePlayerDamage(player)",
        "description": "Prevent player from taking damage (server only)"
    },
    "Register a Custom Tool": {
        "category": "Players",
        "code": 'RegisterTool("tool_id", "Tool Name", "path/to/tool/file", group_number)',
        "description": "Register a custom tool for players (server only)"
    },
    "Set Tool Ammo Pickup Amount": {
        "category": "Players",
        "code": "SetToolAmmoPickupAmount(\"tool_id\", ammo_amount)",
        "description": "Set ammo amount when picking up crates (server only)"
    },
    "Get Tool Ammo Pickup Amount": {
        "category": "Players",
        "code": "local amount = GetToolAmmoPickupAmount(\"tool_id\")",
        "description": "Get ammo pickup amount for a tool"
    },
    "Get Tool's Body": {
        "category": "Players",
        "code": "local body = GetToolBody(player)",
        "description": "Get the physics body of the visible tool"
    },
    "Get Player's Walking Speed": {
        "category": "Players",
        "code": "local walk_speed = GetPlayerWalkingSpeed(player)",
        "description": "Get player's base walking speed"
    },
    "Get Player's Animator": {
        "category": "Players",
        "code": "local animator = GetPlayerAnimator(player)",
        "description": "Get the animator handle for a player"
    },
    "Play Animation Loop": {
        "category": "Animation",
        "code": "PlayAnimationLoop(animator, \"animation_name\")",
        "description": "Play an animation in a continuous loop"
    },
    "Play Single Animation": {
        "category": "Animation",
        "code": "PlayAnimation(animator, \"animation_name\")",
        "description": "Play an animation once"
    },
    "Set Player's Animator": {
        "category": "Players",
        "code": "SetPlayerAnimator(player, animator)",
        "description": "Set the animator for a player"
    },
    "Get Player's Bodies": {
        "category": "Players",
        "code": "local bodies = GetPlayerBodies(player)",
        "description": "Get all bodies owned by a player"
    },
    "Get Tool Hand Poses (Local)": {
        "category": "Players",
        "code": "local right_hand, left_hand = GetToolHandPoseLocalTransform(player)",
        "description": "Get hand positions relative to tool body"
    },
    "Get Tool Hand Poses (World)": {
        "category": "Players",
        "code": "local right_hand, left_hand = GetToolHandPoseWorldTransform(player)",
        "description": "Get hand positions in world space"
    },
    "Set Tool Hand Poses": {
        "category": "Players",
        "code": "SetToolHandPoseLocalTransform(right_hand, left_hand, player)",
        "description": "Override hand poses for tool (client only)"
    },
    "Get Tool Location (Local)": {
        "category": "Players",
        "code": "local transform = GetToolLocationLocalTransform(\"location_name\", player)",
        "description": "Get a tool location in tool space"
    },
    "Get Tool Location (World)": {
        "category": "Players",
        "code": "local transform = GetToolLocationWorldTransform(\"location_name\", player)",
        "description": "Get a tool location in world space"
    },
    "Set Tool Transform": {
        "category": "Players",
        "code": "SetToolTransform(transform, sway_amount, player)",
        "description": "Apply transform to visible tool (client only)"
    },
    "Set Tool Zoom": {
        "category": "Players",
        "code": "SetToolAllowedZoom(zoom_factor, sensitivity)",
        "description": "Set zoom level for a tool (client only)"
    },
    "Override Tool Transform": {
        "category": "Players",
        "code": "SetToolTransformOverride(transform, player)",
        "description": "Replace tool animations with custom transform (client only)"
    },
    "Set Tool Offset": {
        "category": "Players",
        "code": "SetToolOffset(offset_vector, player)",
        "description": "Apply constant offset to tool (client only)"
    },
    "Set Tool Ammo": {
        "category": "Players",
        "code": "SetToolAmmo(\"tool_id\", ammo_amount, player)",
        "description": "Set total ammo reserve for a tool (server only)"
    },
    "Get Tool Ammo": {
        "category": "Players",
        "code": "local ammo = GetToolAmmo(\"tool_id\", player)",
        "description": "Get current ammo for a tool"
    },
    "Enable/Disable Tool": {
        "category": "Players",
        "code": "SetToolEnabled(\"tool_id\", true, player)",
        "description": "Enable or disable a tool for player (server only)"
    },
    "Check if Tool is Enabled": {
        "category": "Players",
        "code": "if IsToolEnabled(\"tool_id\", player) then\n    -- Tool is enabled\nend",
        "description": "Check if a tool is enabled for player"
    },
    "Set Player Orientation": {
        "category": "Players",
        "code": "SetPlayerOrientation(orientation, player)",
        "description": "Set player's base orientation (server only)"
    },
    "Get Player Orientation": {
        "category": "Players",
        "code": "local orientation = GetPlayerOrientation(player)",
        "description": "Get player's base orientation"
    },
    "Get Player's Up Vector": {
        "category": "Players",
        "code": "local up_vector = GetPlayerUp(player)",
        "description": "Get player's up direction vector"
    },
    "Set Player's Rig": {
        "category": "Players",
        "code": "SetPlayerRig(rig_handle, player)",
        "description": "Attach a rig to a player"
    },
    "Get Player's Rig": {
        "category": "Players",
        "code": "local rig = GetPlayerRig(player)",
        "description": "Get the rig assigned to a player"
    },
    "Get Player's Rig Transform": {
        "category": "Players",
        "code": "local transform = GetPlayerRigWorldTransform(player)",
        "description": "Get the world transform of player's rig"
    },
    "Clear Player's Rig": {
        "category": "Players",
        "code": "ClearPlayerRig(rig_id, player)",
        "description": "Remove a rig from player (deprecated)"
    },
    "Set Player Rig Location": {
        "category": "Players",
        "code": "SetPlayerRigLocationLocalTransform(rig_id, \"location_name\", transform, player)",
        "description": "Set rig location transform (deprecated)"
    },
    "Set Player Rig Transform": {
        "category": "Players",
        "code": "SetPlayerRigTransform(rig_id, transform, player)",
        "description": "Set player rig transform (deprecated)"
    },
    "Get Player Rig Location (World)": {
        "category": "Players",
        "code": "local transform = GetPlayerRigLocationWorldTransform(\"location_name\", player)",
        "description": "Get rig location in world space (deprecated)"
    },
    "Set Player Rig Tag": {
        "category": "Players",
        "code": "SetPlayerRigTags(rig_id, \"tag_name\", player)",
        "description": "Add tag to player rig (deprecated)"
    },
    "Check Player Rig Has Tag": {
        "category": "Players",
        "code": "if GetPlayerRigHasTag(\"tag_name\", player) then\n    -- Rig has tag\nend",
        "description": "Check if player rig has tag (deprecated)"
    },
    "Get Player Rig Tag Value": {
        "category": "Players",
        "code": "local value = GetPlayerRigTagValue(\"tag_name\", player)",
        "description": "Get tag value from player rig (deprecated)"
    },
    "Get User Nickname": {
        "category": "Players",
        "code": "local nickname = GetUserNickname(user_id)",
        "description": "Get the nickname of a specific user"
    },


    #audio
    "Play a Sound": {
        "category": "Audio",
        "code": 'PlaySound("sound_name", position, volume)',
        "description": "Play a sound effect at a specific position"
    },
    "Load a Sound": {
        "category": "Audio",
        "code": 'local handle = LoadSound("path/to/sound.ogg", distance)',
        "description": "Load a sound file into memory"
    },
    "Unload a Sound": {
        "category": "Audio",
        "code": "UnloadSound(sound_handle)",
        "description": "Remove a sound from memory"
    },
    "Load a Looping Sound": {
        "category": "Audio",
        "code": 'local handle = LoadLoop("path/to/loop.ogg", distance)',
        "description": "Load a sound file for continuous looping"
    },
    "Unload a Looping Sound": {
        "category": "Audio",
        "code": "UnloadLoop(loop_handle)",
        "description": "Remove a looping sound from memory"
    },
    "Set Loop for Gamepad": {
        "category": "Audio",
        "code": "SetSoundLoopUser(loop_handle, player_index)",
        "description": "Play loop through specific gamepad (client only)"
    },
    "Play Sound for User": {
        "category": "Audio",
        "code": "PlaySoundForUser(sound_handle, player_index, position, volume)",
        "description": "Play sound only for specific player (client only)"
    },
    "Stop a Sound": {
        "category": "Audio",
        "code": 'StopSound("sound_name")',
        "description": "Stop a currently playing sound"
    },
    "Check if Sound is Playing": {
        "category": "Audio",
        "code": "if IsSoundPlaying(sound_handle) then\n    -- Sound is still playing\nend",
        "description": "Check if a sound is currently playing"
    },
    "Get Sound Progress": {
        "category": "Audio",
        "code": "local time = GetSoundProgress(sound_handle)",
        "description": "Get current playback time of a sound"
    },
    "Set Sound Progress": {
        "category": "Audio",
        "code": "SetSoundProgress(sound_handle, time_in_seconds)",
        "description": "Jump to specific time in a sound"
    },
    "Play a Looping Sound": {
        "category": "Audio",
        "code": "PlayLoop(loop_handle, position, volume)",
        "description": "Play a continuous looping sound"
    },
    "Get Loop Progress": {
        "category": "Audio",
        "code": "local time = GetSoundLoopProgress(loop_handle)",
        "description": "Get current playback time of a loop"
    },
    "Set Loop Progress": {
        "category": "Audio",
        "code": "SetSoundLoopProgress(loop_handle, time_in_seconds)",
        "description": "Jump to specific time in a loop"
    },
    "Play Music": {
        "category": "Audio",
        "code": 'PlayMusic("music_name", volume)',
        "description": "Play background music"
    },
    "Stop Music": {
        "category": "Audio",
        "code": "StopMusic()",
        "description": "Stop the currently playing music"
    },
    "Check if Music is Playing": {
        "category": "Audio",
        "code": "if IsMusicPlaying() then\n    -- Music is playing\nend",
        "description": "Check if any music is currently playing"
    },
    "Pause/Resume Music": {
        "category": "Audio",
        "code": "SetMusicPaused(true)",
        "description": "Pause or resume background music"
    },
    "Get Music Progress": {
        "category": "Audio",
        "code": "local time = GetMusicProgress()",
        "description": "Get current playback time of music"
    },
    "Set Music Progress": {
        "category": "Audio",
        "code": "SetMusicProgress(time_in_seconds)",
        "description": "Jump to specific time in music"
    },
    "Set Music Volume": {
        "category": "Audio",
        "code": "SetMusicVolume(volume)",
        "description": "Change the volume of background music"
    },
    "Set Music Low Pass Filter": {
        "category": "Audio",
        "code": "SetMusicLowPass(filter_amount)",
        "description": "Apply low-pass filter to music"
    },


    #graphics
    "Load a Sprite": {
        "category": "Graphics",
        "code": 'local sprite = LoadSprite("image_path.png")',
        "description": "Load a 2D image sprite"
    },
    "Show a Sprite": {
        "category": "Graphics",
        "code": "DrawSprite(sprite, position, size, color)",
        "description": "Draw a 2D sprite in the 3D world"
    },
    "Reset Particle Settings": {
        "category": "Graphics",
        "code": "ParticleReset()",
        "description": "Reset particles to default white smoke"
    },
    "Set Particle Type": {
        "category": "Graphics",
        "code": 'ParticleType("smoke")',
        "description": "Set particle type (plain or smoke)"
    },
    "Set Particle Tile": {
        "category": "Graphics",
        "code": "ParticleTile(tile_index)",
        "description": "Select particle texture tile (0-15)"
    },
    "Set Particle Color": {
        "category": "Graphics",
        "code": "ParticleColor(r, g, b, r_end, g_end, b_end)",
        "description": "Set particle color with optional interpolation"
    },
    "Set Particle Size": {
        "category": "Graphics",
        "code": "ParticleRadius(radius, radius_end, \"linear\", fade_in, fade_out)",
        "description": "Set particle radius with transition effects"
    },
    "Set Particle Opacity": {
        "category": "Graphics",
        "code": "ParticleAlpha(alpha, alpha_end, \"linear\", fade_in, fade_out)",
        "description": "Set particle transparency with transitions"
    },
    "Set Particle Gravity": {
        "category": "Graphics",
        "code": "ParticleGravity(gravity, end_gravity, \"linear\", fade_in, fade_out)",
        "description": "Set how gravity affects particles"
    },
    "Set Particle Drag": {
        "category": "Graphics",
        "code": "ParticleDrag(drag, end_drag, \"linear\", fade_in, fade_out)",
        "description": "Set air resistance on particles"
    },
    "Make Particles Glow": {
        "category": "Graphics",
        "code": "ParticleEmissive(glow_amount, end_glow, \"linear\", fade_in, fade_out)",
        "description": "Make particles emit light"
    },
    "Set Particle Rotation": {
        "category": "Graphics",
        "code": "ParticleRotation(rotation_speed, end_speed, \"linear\", fade_in, fade_out)",
        "description": "Set particle rotation speed"
    },
    "Stretch Particles": {
        "category": "Graphics",
        "code": "ParticleStretch(stretch_amount, end_stretch, \"linear\", fade_in, fade_out)",
        "description": "Stretch particles along motion"
    },
    "Set Particle Stickiness": {
        "category": "Graphics",
        "code": "ParticleSticky(stickiness, end_stickiness, \"linear\", fade_in, fade_out)",
        "description": "Control how particles stick to surfaces"
    },
    "Set Particle Collisions": {
        "category": "Graphics",
        "code": "ParticleCollide(collision_strength, end_strength, \"linear\", fade_in, fade_out)",
        "description": "Control particle collision strength"
    },
    "Set Particle Flags": {
        "category": "Graphics",
        "code": "ParticleFlags(256)",
        "description": "Set special particle flags (256 for fire extinguishing)"
    },
    "Spawn a Particle": {
        "category": "Graphics",
        "code": "SpawnParticle(position, velocity, lifetime)",
        "description": "Create a single particle with current settings"
    },
    "Draw a 3D Line": {
        "category": "Graphics",
        "code": "DrawLine(start_point, end_point, r, g, b, a)",
        "description": "Draw a visible line in 3D space"
    },
    "Draw Debug Line": {
        "category": "Graphics",
        "code": "DebugLine(start_point, end_point, r, g, b, a)",
        "description": "Draw a debug line (hidden behind objects)"
    },
    "Draw Debug Cross": {
        "category": "Graphics",
        "code": "DebugCross(position, r, g, b, a)",
        "description": "Draw a cross marker at a position"
    },
    "Draw Transform Axes": {
        "category": "Graphics",
        "code": "DebugTransform(transform, scale)",
        "description": "Draw X/Y/Z axes at a transform"
    },
    "Show Debug Value": {
        "category": "Graphics",
        "code": "DebugWatch(\"variable_name\", value, wrap_lines)",
        "description": "Display a value on screen for debugging"
    },
    "Print Debug Message": {
        "category": "Graphics",
        "code": "DebugPrint(\"message\", wrap_lines)",
        "description": "Print text to debug overlay"
    },
    "Draw Shape Outline": {
        "category": "Graphics",
        "code": "DrawShapeOutline(shape)",
        "description": "Draw an outline around a shape for one frame"
    },
    "Highlight Shape": {
        "category": "Graphics",
        "code": "DrawShapeHighlight(shape)",
        "description": "Flash/highlight a shape for one frame"
    },


    #UI
    "Find a Screen": {
        "category": "UI",
        "code": 'local screen = FindScreen("screen_name")',
        "description": "Find a UI screen by its tag name"
    },
    "Find All Screens": {
        "category": "UI",
        "code": 'local screens = FindScreens("screen_name")',
        "description": "Find all UI screens with a specific tag"
    },
    "Turn a Screen On/Off": {
        "category": "UI",
        "code": "SetScreenEnabled(screen, true)",
        "description": "Enable or disable a UI screen (server only)"
    },
    "Check if a Screen is On": {
        "category": "UI",
        "code": "if IsScreenEnabled(screen) then\n    -- Screen is enabled\nend",
        "description": "Check if a UI screen is currently enabled"
    },
    "Get a Screen's Shape": {
        "category": "UI",
        "code": "local shape = GetScreenShape(screen)",
        "description": "Get the shape that owns a UI screen"
    },
    "Enable UI Interaction": {
        "category": "UI",
        "code": "UiMakeInteractive()",
        "description": "Enable mouse and UI interaction"
    },
    "Push UI State": {
        "category": "UI",
        "code": "UiPush()",
        "description": "Save current UI state to stack"
    },
    "Pop UI State": {
        "category": "UI",
        "code": "UiPop()",
        "description": "Restore previous UI state from stack"
    },
    "Get UI Width": {
        "category": "UI",
        "code": "local width = UiWidth()",
        "description": "Get current UI drawing width"
    },
    "Get UI Height": {
        "category": "UI",
        "code": "local height = UiHeight()",
        "description": "Get current UI drawing height"
    },
    "Get UI Center": {
        "category": "UI",
        "code": "local center_x, center_y = UiCenter()",
        "description": "Get center coordinates of UI area"
    },
    "Get UI Middle": {
        "category": "UI",
        "code": "local middle = UiMiddle()",
        "description": "Get middle height of UI area"
    },
    "Set UI Color": {
        "category": "UI",
        "code": "UiColor(r, g, b, a)",
        "description": "Set color for UI drawing"
    },
    "Set UI Color Filter": {
        "category": "UI",
        "code": "UiColorFilter(r, g, b, a)",
        "description": "Apply color filter to UI elements"
    },
    "Reset UI Colors": {
        "category": "UI",
        "code": "UiResetColor()",
        "description": "Reset UI colors to defaults"
    },
    "Move UI Cursor": {
        "category": "UI",
        "code": "UiTranslate(x, y)",
        "description": "Move UI drawing cursor"
    },
    "Rotate UI Cursor": {
        "category": "UI",
        "code": "UiRotate(angle_degrees)",
        "description": "Rotate UI drawing cursor"
    },
    "Scale UI Cursor": {
        "category": "UI",
        "code": "UiScale(x_scale, y_scale)",
        "description": "Scale UI drawing cursor"
    },
    "Get UI Scale": {
        "category": "UI",
        "code": "local x_scale, y_scale = UiGetScale()",
        "description": "Get current UI scale values"
    },
    "Set UI Clipping": {
        "category": "UI",
        "code": "UiClipRect(x, y, width, height)",
        "description": "Set clipping rectangle for UI"
    },
    "Create UI Window": {
        "category": "UI",
        "code": "UiWindow(x, y, width, height, \"style\")",
        "description": "Create a UI window area"
    },
    "Get Current UI Window": {
        "category": "UI",
        "code": "local window_info = UiGetCurrentWindow()",
        "description": "Get current window boundaries"
    },
    "Check Point in Window": {
        "category": "UI",
        "code": "if UiIsInCurrentWindow(x, y) then\n    -- Point is in window\nend",
        "description": "Check if point is in current window"
    },
    "Check Rectangle Clipped": {
        "category": "UI",
        "code": "if UiIsRectFullyClipped(x, y, width, height) then\n    -- Rectangle is clipped\nend",
        "description": "Check if rectangle is fully clipped"
    },
    "Check Point in Clip Region": {
        "category": "UI",
        "code": "if UiIsInClipRegion(x, y) then\n    -- Point is visible\nend",
        "description": "Check if point is in clipping region"
    },
    "Check Cursor Clipped": {
        "category": "UI",
        "code": "if UiIsFullyClipped() then\n    -- Cursor is clipped\nend",
        "description": "Check if current position is clipped"
    },
    "Get Safe UI Area": {
        "category": "UI",
        "code": "local x1, y1, x2, y2 = UiSafeMargins()",
        "description": "Get safe drawing area coordinates"
    },
    "Get Canvas Size": {
        "category": "UI",
        "code": "local width, height = UiCanvasSize()",
        "description": "Get UI canvas dimensions"
    },
    "Set UI Alignment": {
        "category": "UI",
        "code": 'UiAlign("center middle")',
        "description": "Set alignment for UI elements"
    },
    "Set Text Alignment": {
        "category": "UI",
        "code": 'UiTextAlignment("center")',
        "description": "Set text alignment"
    },
    "Begin Modal UI": {
        "category": "UI",
        "code": "UiModalBegin()",
        "description": "Start modal UI state"
    },
    "End Modal UI": {
        "category": "UI",
        "code": "UiModalEnd()",
        "description": "End modal UI state"
    },
    "Disable UI Input": {
        "category": "UI",
        "code": "UiDisableInput()",
        "description": "Disable UI input"
    },
    "Enable UI Input": {
        "category": "UI",
        "code": "UiEnableInput()",
        "description": "Enable UI input"
    },
    "Check UI Receives Input": {
        "category": "UI",
        "code": "if UiReceivesInput() then\n    -- UI can receive input\nend",
        "description": "Check if UI accepts input"
    },
    "Get Mouse Position": {
        "category": "UI",
        "code": "local mouse_x, mouse_y = UiGetMousePos()",
        "description": "Get mouse screen coordinates"
    },
    "Get Canvas Mouse Position": {
        "category": "UI",
        "code": "local canvas_x, canvas_y = UiGetCanvasMousePos()",
        "description": "Get mouse canvas coordinates"
    },
    "Check Mouse in Rectangle": {
        "category": "UI",
        "code": "if UiIsMouseInRect(x, y, width, height) then\n    -- Mouse is in rectangle\nend",
        "description": "Check if mouse is in rectangle"
    },
    "Convert World to Screen": {
        "category": "UI",
        "code": "local screen_x, screen_y = UiWorldToPixel(world_position)",
        "description": "Convert world coordinates to screen"
    },
    "Convert Screen to World": {
        "category": "UI",
        "code": "local world_pos = UiPixelToWorld(screen_x, screen_y)",
        "description": "Convert screen coordinates to world"
    },
    "Get UI Cursor Position": {
        "category": "UI",
        "code": "local cursor_x, cursor_y = UiGetCursorPos()",
        "description": "Get current UI cursor position"
    },
    "Apply UI Blur": {
        "category": "UI",
        "code": "UiBlur(blur_amount)",
        "description": "Apply blur effect to UI"
    },
    "Set UI Font": {
        "category": "UI",
        "code": 'UiFont("path/to/font.ttf")',
        "description": "Set font for UI text"
    },
    "Get Font Height": {
        "category": "UI",
        "code": "local height = UiFontHeight()",
        "description": "Get current font height"
    },
    "Draw UI Text": {
        "category": "UI",
        "code": 'UiText("Hello World")',
        "description": "Draw text at cursor position"
    },
    "Disable Text Wildcards": {
        "category": "UI",
        "code": "UiTextDisableWildcards(true)",
        "description": "Disable special character substitution"
    },
    "Set Uniform Text Height": {
        "category": "UI",
        "code": "UiTextUniformHeight(true)",
        "description": "Enable uniform text line height"
    },
    "Get Text Size": {
        "category": "UI",
        "code": "local width, height = UiGetTextSize(\"text\")",
        "description": "Get text dimensions"
    },
    "Measure Text": {
        "category": "UI",
        "code": "local width, height = UiMeasureText(\"text\")",
        "description": "Measure text dimensions"
    },
    "Count Text Symbols": {
        "category": "UI",
        "code": "local count = UiGetSymbolsCount(\"text\")",
        "description": "Count special symbols in text"
    },
    "Substitute Text Symbols": {
        "category": "UI",
        "code": "UiTextSymbolsSub(\"text\", start_pos, count, \"substitution\")",
        "description": "Replace symbols in text"
    },
    "Wrap Text": {
        "category": "UI",
        "code": "local wrapped_text = UiWordWrap(\"long text\", max_width)",
        "description": "Wrap text to fit width"
    },
    "Set Text Line Spacing": {
        "category": "UI",
        "code": "UiTextLineSpacing(spacing)",
        "description": "Set spacing between text lines"
    },
    "Draw Text Outline": {
        "category": "UI",
        "code": "UiTextOutline(x, y, thickness)",
        "description": "Draw text outline"
    },
    "Draw Text Shadow": {
        "category": "UI",
        "code": "UiTextShadow(x, y, blur)",
        "description": "Draw text shadow"
    },
    "Draw UI Rectangle": {
        "category": "UI",
        "code": "UiRect(x, y, width, height)",
        "description": "Draw filled rectangle"
    },
    "Draw Rectangle Outline": {
        "category": "UI",
        "code": "UiRectOutline(x, y, width, height)",
        "description": "Draw rectangle border"
    },
    "Draw Rounded Rectangle": {
        "category": "UI",
        "code": "UiRoundedRect(x, y, width, height, radius)",
        "description": "Draw filled rounded rectangle"
    },
    "Draw Rounded Outline": {
        "category": "UI",
        "code": "UiRoundedRectOutline(x, y, width, height, radius)",
        "description": "Draw rounded rectangle border"
    },
    "Draw UI Circle": {
        "category": "UI",
        "code": "UiCircle(x, y, radius)",
        "description": "Draw filled circle"
    },
    "Draw Circle Outline": {
        "category": "UI",
        "code": "UiCircleOutline(x, y, radius)",
        "description": "Draw circle border"
    },
    "Fill Screen with Image": {
        "category": "UI",
        "code": 'UiFillImage("path/to/image.png")',
        "description": "Fill screen with image"
    },
    "Apply Background Blur": {
        "category": "UI",
        "code": "UiBackgroundBlur(blur_amount)",
        "description": "Apply background blur effect"
    },
    "Draw UI Image": {
        "category": "UI",
        "code": 'UiImage("path/to/image.png")',
        "description": "Draw image at cursor"
    },
    "Unload UI Image": {
        "category": "UI",
        "code": 'UiUnloadImage("path/to/image.png")',
        "description": "Remove image from memory"
    },
    "Check if Image Loaded": {
        "category": "UI",
        "code": 'if UiHasImage("path/to/image.png") then\n    -- Image is loaded\nend',
        "description": "Check if image exists and is loaded"
    },
    "Get Image Size": {
        "category": "UI",
        "code": 'local width, height = UiGetImageSize("path/to/image.png")',
        "description": "Get image dimensions"
    },
    "Draw Image Box": {
        "category": "UI",
        "code": 'UiImageBox("path/to/image.png", x, y, width, height, u1, v1, u2, v2)',
        "description": "Draw image with UV coordinates"
    },
    "Play UI Sound": {
        "category": "UI",
        "code": 'UiSound("path/to/sound.ogg", volume)',
        "description": "Play UI sound effect"
    },
    "Play UI Sound Loop": {
        "category": "UI",
        "code": 'UiSoundLoop("path/to/sound.ogg", volume)',
        "description": "Play looping UI sound"
    },
    "Mute UI Sounds": {
        "category": "UI",
        "code": "UiMute(true)",
        "description": "Mute or unmute UI sounds"
    },
    "Create Button with Image Background": {
        "category": "UI",
        "code": 'UiButtonImageBox("path/to/image.png", x, y, width, height)',
        "description": "Create button with image background"
    },
    "Set Button Hover Color": {
        "category": "UI",
        "code": "UiButtonHoverColor(r, g, b, a)",
        "description": "Set button hover color"
    },
    "Set Button Press Color": {
        "category": "UI",
        "code": "UiButtonPressColor(r, g, b, a)",
        "description": "Set button press color"
    },
    "Set Button Press Distance": {
        "category": "UI",
        "code": "UiButtonPressDist(distance)",
        "description": "Set button press offset"
    },
    "Set Button Text Handling": {
        "category": "UI",
        "code": 'UiButtonTextHandling("truncate")',
        "description": "Set how buttons handle text overflow"
    },
    "Create Text Button": {
        "category": "UI",
        "code": 'local clicked = UiTextButton("Click Me", x, y, width, height, click_function)',
        "description": "Create interactive text button"
    },
    "Create Interactive Image Button": {
        "category": "UI",
        "code": 'local clicked = UiImageButton("path/to/image.png", x, y, width, height, click_function)',
        "description": "Create interactive image button"
    },
    "Create Blank Button": {
        "category": "UI",
        "code": 'local clicked = UiBlankButton(x, y, width, height, click_function)',
        "description": "Create invisible interactive button"
    },
    "Create Slider": {
        "category": "UI",
        "code": 'local value, changed = UiSlider("path/to/image.png", "horizontal", current_value, min_value, max_value)',
        "description": "Create interactive slider"
    },
    "Set Slider Hover Color": {
        "category": "UI",
        "code": "UiSliderHoverColorFilter(r, g, b, a)",
        "description": "Set slider hover color"
    },
    "Set Slider Thumb Size": {
        "category": "UI",
        "code": "UiSliderThumbSize(width, height)",
        "description": "Set slider thumb dimensions"
    },
    "Get Screen Size": {
        "category": "UI",
        "code": "local screen_size = UiGetScreen()",
        "description": "Get screen dimensions"
    },
    "Create Navigation Component": {
        "category": "UI",
        "code": "local component_id = UiNavComponent(width, height)",
        "description": "Create navigation component for gamepad"
    },
    "Ignore Navigation": {
        "category": "UI",
        "code": "UiIgnoreNavigation(true)",
        "description": "Ignore navigation for current scope"
    },
    "Reset Navigation": {
        "category": "UI",
        "code": "UiResetNavigation()",
        "description": "Reset navigation state"
    },
    "Skip Navigation Update": {
        "category": "UI",
        "code": "UiNavSkipUpdate()",
        "description": "Skip navigation update this frame"
    },
    "Check Component Focus": {
        "category": "UI",
        "code": "if UiIsComponentInFocus(component_id) then\n    -- Component is focused\nend",
        "description": "Check if component has focus"
    },
    "Begin Navigation Group": {
        "category": "UI",
        "code": "local group_id = UiNavGroupBegin(\"group_id\")",
        "description": "Start navigation group"
    },
    "End Navigation Group": {
        "category": "UI",
        "code": "UiNavGroupEnd()",
        "description": "End navigation group"
    },
    "Set Navigation Group Size": {
        "category": "UI",
        "code": "UiNavGroupSize(width, height)",
        "description": "Set navigation group dimensions"
    },
    "Force Component Focus": {
        "category": "UI",
        "code": "UiForceFocus(component_id)",
        "description": "Force focus on component"
    },
    "Get Focused Component ID": {
        "category": "UI",
        "code": "local focused_id = UiFocusedComponentId()",
        "description": "Get ID of focused component"
    },
    "Get Focused Component Rect": {
        "category": "UI",
        "code": "local rect = UiFocusedComponentRect(index)",
        "description": "Get focused component rectangle"
    },
    "Get UI Item Size": {
        "category": "UI",
        "code": "local width, height = UiGetItemSize()",
        "description": "Get UI item dimensions"
    },
    "Enable Auto Translation": {
        "category": "UI",
        "code": "UiAutoTranslate()",
        "description": "Enable automatic text translation"
    },
    "Begin UI Frame": {
        "category": "UI",
        "code": "UiBeginFrame()",
        "description": "Begin UI frame for layout"
    },
    "Reset UI Frame": {
        "category": "UI",
        "code": "UiResetFrame()",
        "description": "Reset UI frame state"
    },
    "Occupy Frame Area": {
        "category": "UI",
        "code": "UiFrameOccupy(x, y, width, height)",
        "description": "Reserve area in UI frame"
    },
    "End UI Frame": {
        "category": "UI",
        "code": "UiEndFrame()",
        "description": "End UI frame"
    },
    "Skip Frame Item": {
        "category": "UI",
        "code": "UiFrameSkipItem(true)",
        "description": "Skip item in frame layout"
    },
    "Get Frame Number": {
        "category": "UI",
        "code": "local frame_no = UiGetFrameNo()",
        "description": "Get current frame number"
    },
    "Get UI Language": {
        "category": "UI",
        "code": "local language = UiGetLanguage()",
        "description": "Get current UI language"
    },
    "Set Cursor State": {
        "category": "UI",
        "code": "UiSetCursorState(state)",
        "description": "Set cursor interaction state"
    },
    "Add a Pause Menu Button": {
        "category": "UI",
        "code": 'local pressed = PauseMenuButton("Button Title", "main_bottom", false)',
        "description": "Add a button to the pause menu (call every frame)"
    },
    "Hide and Lock Cursor": {
        "category": "UI",
        "code": "UiSetCursorState(UI_CURSOR_HIDE_AND_LOCK)",
        "description": "Hide cursor and lock it (for gamepad navigation)"
    },
    "Make UI Interactive": {
        "category": "UI",
        "code": "UiMakeInteractive()",
        "description": "Enable mouse and UI interaction"
    },


    #game control
    "Get a Script Parameter": {
        "category": "Game Control",
        "code": 'local value = GetIntParam("parameter_name", default_value)',
        "description": "Get a parameter value from the level XML file"
    },
    "Get a Text Parameter": {
        "category": "Game Control",
        "code": 'local text = GetStringParam("parameter_name", "default_text")',
        "description": "Get a text parameter from the level XML file"
    },
    "Get a True/False Parameter": {
        "category": "Game Control",
        "code": 'local enabled = GetBoolParam("parameter_name", false)',
        "description": "Get a boolean parameter from the level XML file"
    },
    "Get a Decimal Parameter": {
        "category": "Game Control",
        "code": 'local value = GetFloatParam("parameter_name", 1.0)',
        "description": "Get a decimal number parameter from the level XML file"
    },
    "Get a Color Parameter": {
        "category": "Game Control",
        "code": 'local r, g, b, a = GetColorParam("parameter_name", {1, 1, 1, 1})',
        "description": "Get a color parameter from the level XML file"
    },
    "Get the Game's Version": {
        "category": "Game Control",
        "code": "local version = GetVersion()",
        "description": "Get the current Teardown version string"
    },
    "Check for the Game's Version": {
        "category": "Game Control",
        "code": 'if HasVersion("0.6.0") then\n    -- Code for version 0.6.0 or newer\nend',
        "description": "Check if the game version is at least a certain version"
    },
    "Set a Value with Animation": {
        "category": "Game Control",
        "code": 'SetValue("variable_name", new_value, "linear", 1.0)',
        "description": "Set a global variable with animated transition"
    },
    "Set a Table Value with Animation": {
        "category": "Game Control",
        "code": "SetValueInTable(table, member_name, new_value, type, length)",
        "description": "Animate a value change in a global table"
    },
    "Check if File Exists": {
        "category": "Game Control",
        "code": 'if HasFile("path/to/file.txt") then\n    -- File exists\nend',
        "description": "Check if a file exists at the specified path"
    },
    "Start a Level": {
        "category": "Game Control",
        "code": 'StartLevel("mission_name", "path/to/level", "layers", false)',
        "description": "Start a level with optional layers and loading screen"
    },
    "Pause the Game": {
        "category": "Game Control",
        "code": "SetPaused(true)",
        "description": "Pause or unpause the game"
    },
    "Restart the Level": {
        "category": "Game Control",
        "code": "Restart()",
        "description": "Restart the current level"
    },
    "Go to the Main Menu": {
        "category": "Game Control",
        "code": "Menu()",
        "description": "Go back to the main menu"
    },
    "Load Haptic Effect": {
        "category": "Game Control",
        "code": 'local handle = LoadHaptic("path/to/haptic.file")',
        "description": "Load vibration effect file (client only)"
    },
    "Create Haptic Effect": {
        "category": "Game Control",
        "code": "local handle = CreateHaptic(left_motor, right_motor, left_trigger, right_trigger)",
        "description": "Create custom vibration effect (client only)"
    },
    "Play Haptic Effect": {
        "category": "Game Control",
        "code": "PlayHaptic(handle, amplitude)",
        "description": "Play vibration effect (client only)"
    },
    "Play Directional Haptic": {
        "category": "Game Control",
        "code": "PlayHapticDirectional(handle, direction, amplitude)",
        "description": "Play directional vibration (client only)"
    },
    "Check if Haptic Playing": {
        "category": "Game Control",
        "code": "if HapticIsPlaying(handle) then\n    -- Haptic is active\nend",
        "description": "Check if vibration is playing (client only)"
    },
    "Set Tool Haptic": {
        "category": "Game Control",
        "code": 'SetToolHaptic("tool_id", haptic_handle, amplitude)',
        "description": "Link vibration to tool (client only)"
    },
    "Stop Haptic Effect": {
        "category": "Game Control",
        "code": "StopHaptic(handle)",
        "description": "Stop vibration effect (client only)"
    },
    "Apply Heat to Shape": {
        "category": "Game Control",
        "code": "AddHeat(shape, position, heat_amount)",
        "description": "Apply heat like a blowtorch (server only)"
    },
    "Get Level Area": {
        "category": "Game Control",
        "code": "local area = GetBoundaryArea()",
        "description": "Get the area of the level boundary"
    },
    "Get Level Bounds": {
        "category": "Game Control",
        "code": "local min_bound, max_bound = GetBoundaryBounds()",
        "description": "Get the bounding box of the level"
    },
    "Get Gravity": {
        "category": "Game Control",
        "code": "local gravity = GetGravity()",
        "description": "Get current gravity vector"
    },
    "Set Gravity": {
        "category": "Game Control",
        "code": "SetGravity(gravity_vector)",
        "description": "Change world gravity (server only)"
    },
    "Get FPS": {
        "category": "Game Control",
        "code": "local fps = GetFps()",
        "description": "Get current frames per second"
    },
    "Spawn an Object": {
        "category": "Game Control",
        "code": 'Spawn(xml_string, transform, allow_static, joint_existing)',
        "description": "Spawn a prefab or XML snippet in the world"
    },
    "Spawn a Layer": {
        "category": "Game Control",
        "code": 'SpawnLayer(xml_file, "layer_name", transform, allow_static, joint_existing)',
        "description": "Spawn a specific layer from a VOX/XML file"
    },
    "Spawn a Tool": {
        "category": "Game Control",
        "code": 'SpawnTool("tool_id", transform, allow_static, voxel_scale)',
        "description": "Spawn a registered tool at a position"
    },
    "Add Map Marker": {
        "category": "Game Control",
        "code": "AddMapMarker(id, \"tag\", \"name\", \"category\", show_label, \"info\", position, color, \"info_image\", \"dot_icon\")",
        "description": "Add a custom marker to the map (client only)"
    },
    "Get Selected Map Marker": {
        "category": "Game Control",
        "code": "local marker_id, tag = SelectedMapMarker()",
        "description": "Get which map marker player selected (client only)"
    },
    "Shoot Projectile": {
        "category": "Game Control",
        "code": "Shoot(origin, direction, \"type\", strength, max_distance, player)",
        "description": "Fire a projectile (server only)"
    },
    "Paint Area": {
        "category": "Game Control",
        "code": "Paint(position, radius, \"type\", probability)",
        "description": "Paint nearby geometry (server only)"
    },
    "Paint Area with Color": {
        "category": "Game Control",
        "code": "PaintRGBA(position, radius, r, g, b, alpha, probability)",
        "description": "Tint geometry with custom color (server only)"
    },
    "Make a Hole": {
        "category": "Game Control",
        "code": "local voxels_removed = MakeHole(position, soft_radius, medium_radius, hard_radius, silent)",
        "description": "Cut a hole by removing voxels (server only)"
    },
    "Create Explosion": {
        "category": "Game Control",
        "code": "Explosion(position, size)",
        "description": "Create an explosion (server only)"
    },
    "Start Fire": {
        "category": "Game Control",
        "code": "SpawnFire(position)",
        "description": "Start a fire at position (server only)"
    },
    "Count Active Fires": {
        "category": "Game Control",
        "code": "local fire_count = GetFireCount()",
        "description": "Get total number of active fires"
    },
    "Find Closest Fire": {
        "category": "Game Control",
        "code": "local found, fire_pos = QueryClosestFire(origin, max_distance)",
        "description": "Find nearest fire within distance"
    },
    "Count Fires in Area": {
        "category": "Game Control",
        "code": "local count = QueryAabbFireCount(min_corner, max_corner)",
        "description": "Count fires inside a bounding box"
    },
    "Remove Fires in Area": {
        "category": "Game Control",
        "code": "local removed = RemoveAabbFires(min_corner, max_corner)",
        "description": "Remove all fires in area (server only)"
    },
    "Get Camera Position": {
        "category": "Game Control",
        "code": "local transform = GetCameraTransform()",
        "description": "Get current camera transform (client only)"
    },
    "Set Camera Position": {
        "category": "Game Control",
        "code": "SetCameraTransform(transform, fov)",
        "description": "Override camera position (client only)"
    },
    "Force First Person View": {
        "category": "Game Control",
        "code": "RequestFirstPerson(smooth_transition)",
        "description": "Switch to first-person view (client only)"
    },
    "Force Third Person View": {
        "category": "Game Control",
        "code": "RequestThirdPerson(smooth_transition)",
        "description": "Switch to third-person view (client only)"
    },
    "Offset Camera": {
        "category": "Game Control",
        "code": "SetCameraOffsetTransform(offset_transform, stackable)",
        "description": "Apply camera offset for shake/wobble (client only)"
    },
    "Attach Camera to Object": {
        "category": "Game Control",
        "code": "AttachCameraTo(object_handle, ignore_rotation)",
        "description": "Attach camera to body/shape (client only)"
    },
    "Set Camera Pivot": {
        "category": "Game Control",
        "code": "SetPivotClipBody(body_handle, main_shape_index)",
        "description": "Set camera clipping pivot (client only)"
    },
    "Shake Camera": {
        "category": "Game Control",
        "code": "ShakeCamera(strength)",
        "description": "Apply camera shake effect (client only)"
    },
    "Set Camera FOV": {
        "category": "Game Control",
        "code": "SetCameraFov(degrees)",
        "description": "Change camera field of view (client only)"
    },
    "Set Camera Blur": {
        "category": "Game Control",
        "code": "SetCameraDof(focus_distance, blur_amount)",
        "description": "Set depth of field blur (client only)"
    },
    "Set Low Health Blur": {
        "category": "Game Control",
        "code": "SetLowHealthBlurThreshold(health_threshold)",
        "description": "Adjust health blur effect (client only)"
    },
    "Add Point Light": {
        "category": "Game Control",
        "code": "PointLight(position, r, g, b, intensity)",
        "description": "Add temporary point light (client only)"
    },
    "Set Game Speed": {
        "category": "Game Control",
        "code": "SetTimeScale(speed_scale)",
        "description": "Slow down or speed up game time (server only)"
    },
    "Reset Environment": {
        "category": "Game Control",
        "code": "SetEnvironmentDefault()",
        "description": "Reset environment to defaults (server only)"
    },
    "Set Environment Property": {
        "category": "Game Control",
        "code": "SetEnvironmentProperty(\"property_name\", value1, value2, value3, value4)",
        "description": "Change environment settings (server only)"
    },
    "Get Environment Property": {
        "category": "Game Control",
        "code": "local value1, value2, value3, value4, value5 = GetEnvironmentProperty(\"property_name\")",
        "description": "Get current environment property values"
    },
    "Reset Post Processing": {
        "category": "Game Control",
        "code": "SetPostProcessingDefault()",
        "description": "Reset post-processing effects to defaults"
    },
    "Set Post Processing": {
        "category": "Game Control",
        "code": "SetPostProcessingProperty(\"property_name\", value1, value2, value3)",
        "description": "Modify post-processing effects"
    },
    "Get Post Processing": {
        "category": "Game Control",
        "code": "local value1, value2, value3 = GetPostProcessingProperty(\"property_name\")",
        "description": "Get current post-processing values"
    },
    "Set Query Required Layers": {
        "category": "Game Control",
        "code": 'QueryRequire("physical,dynamic,static")',
        "description": "Set required layers for scene queries"
    },
    "Set Query Include Layers": {
        "category": "Game Control",
        "code": 'QueryInclude("player,tool")',
        "description": "Include additional layers in queries"
    },
    "Set Query Collision Mask": {
        "category": "Game Control",
        "code": "QueryCollisionMask(255)",
        "description": "Set collision mask filter for queries"
    },
    "Exclude Animator from Query": {
        "category": "Game Control",
        "code": "QueryRejectAnimator(animator_handle)",
        "description": "Exclude specific animator from queries"
    },
    "Exclude Vehicle from Query": {
        "category": "Game Control",
        "code": "QueryRejectVehicle(vehicle_handle)",
        "description": "Exclude vehicle from queries"
    },
    "Exclude Body from Query": {
        "category": "Game Control",
        "code": "QueryRejectBody(body_handle)",
        "description": "Exclude specific body from queries"
    },
    "Exclude Bodies from Query": {
        "category": "Game Control",
        "code": "QueryRejectBodies(body_list)",
        "description": "Exclude multiple bodies from queries"
    },
    "Exclude Shape from Query": {
        "category": "Game Control",
        "code": "QueryRejectShape(shape_handle)",
        "description": "Exclude specific shape from queries"
    },
    "Exclude Shapes from Query": {
        "category": "Game Control",
        "code": "QueryRejectShapes(shape_list)",
        "description": "Exclude multiple shapes from queries"
    },
    "Exclude Player from Query": {
        "category": "Game Control",
        "code": "QueryRejectPlayer(player_id)",
        "description": "Exclude player from queries"
    },
    "Raycast Query": {
        "category": "Game Control",
        "code": "local hit, shape, point, normal = QueryRaycast(origin, direction, max_distance, radius)",
        "description": "Cast a ray/sphere and detect collisions"
    },
    "Raycast Rope Query": {
        "category": "Game Control",
        "code": "local hit, rope_joint, point = QueryRaycastRope(origin, direction, max_distance)",
        "description": "Raycast that detects ropes"
    },
    "Raycast Water Query": {
        "category": "Game Control",
        "code": "local hit, point, normal = QueryRaycastWater(origin, direction, max_distance)",
        "description": "Raycast that detects water surfaces"
    },
    "Projectile Query": {
        "category": "Game Control",
        "code": "local hit, shape, player, damage, point, normal = QueryShot(origin, direction, max_distance, radius)",
        "description": "Check if projectile would hit something"
    },
    "Closest Point Query": {
        "category": "Game Control",
        "code": "local hit, point, normal, shape = QueryClosestPoint(origin, max_distance)",
        "description": "Find closest point on collidable shapes"
    },
    "Get Shapes in Area": {
        "category": "Game Control",
        "code": "local shapes = QueryAabbShapes(min_corner, max_corner)",
        "description": "Get all shapes in a bounding box"
    },
    "Get Bodies in Area": {
        "category": "Game Control",
        "code": "local bodies = QueryAabbBodies(min_corner, max_corner)",
        "description": "Get all bodies in a bounding box"
    },
    "Plan Path": {
        "category": "Game Control",
        "code": "QueryPath(start_point, target_point, max_distance, target_radius, \"type\")",
        "description": "Start pathfinding calculation"
    },
    "Create Path Planner": {
        "category": "Game Control",
        "code": "local planner = CreatePathPlanner()",
        "description": "Create reusable path planner instance"
    },
    "Delete Path Planner": {
        "category": "Game Control",
        "code": "DeletePathPlanner(planner_id)",
        "description": "Remove path planner to free memory"
    },
    "Plan Path with Planner": {
        "category": "Game Control",
        "code": "PathPlannerQuery(planner_id, start_point, target_point, max_distance, target_radius, \"type\")",
        "description": "Plan path using specific planner"
    },
    "Abort Path Planning": {
        "category": "Game Control",
        "code": "AbortPath(planner_id)",
        "description": "Stop current pathfinding calculation"
    },
    "Get Path Planning State": {
        "category": "Game Control",
        "code": "local state = GetPathState(planner_id)",
        "description": "Get status of path planning (idle/busy/fail/done)"
    },
    "Get Path Length": {
        "category": "Game Control",
        "code": "local length = GetPathLength(planner_id)",
        "description": "Get length of calculated path in meters"
    },
    "Get Point on Path": {
        "category": "Game Control",
        "code": "local point = GetPathPoint(distance_along_path, planner_id)",
        "description": "Get position at specific distance along path"
    },
    "Get Loudest Sound": {
        "category": "Game Control",
        "code": "local volume, position = GetLastSound()",
        "description": "Get loudest sound from last frame"
    },
    "Check if Point is in Water": {
        "category": "Game Control",
        "code": "local in_water, depth = IsPointInWater(point)",
        "description": "Check if position is underwater and get depth"
    },
    "Get Wind at Position": {
        "category": "Game Control",
        "code": "local wind = GetWindVelocity(point)",
        "description": "Get wind vector at specific position"
    },
    "Get the Game Time": {
        "category": "Game Control",
        "code": "local time = GetTime()",
        "description": "Get the current game time in seconds"
    },
    "Get Screen's Player": {
        "category": "Game Control",
        "code": "local player = GetScreenPlayer(screen)",
        "description": "Get the player who owns this screen"
    },
    "Call Client Function": {
        "category": "Game Control",
        "code": "ClientCall(player, \"function_name\", param1, param2)",
        "description": "Call function on specific client or all clients"
    },
    "Call Server Function": {
        "category": "Game Control",
        "code": 'ServerCall("function_name", param1, param2)',
        "description": "Call function on server from client"
    },
    "Get the Frame Time": {
        "category": "Game Control", 
        "code": "local timestep = GetTimeStep()",
        "description": "Get the time step for the current frame"
    },
    "Get Translated Text": {
        "category": "Game Control",
        "code": 'local text = GetTranslatedStringByKey("key_name", "default_text")',
        "description": "Get translated text for the current language"
    },
    "Check if Translation Exists": {
        "category": "Game Control",
        "code": 'if HasTranslationByKey("key_name") then\n    -- Translation exists\nend',
        "description": "Check if a translation key exists for the current language"
    },
    "Load Language": {
        "category": "Game Control",
        "code": "LoadLanguageTable(language_id)",
        "description": "Load language table (0=English, 1=French, 2=Spanish, etc.)"
    },
    "Check if File Exists": {
        "category": "Game Control",
        "code": "if HasFile(\"path/to/file.txt\") then\n    -- File exists\nend",
        "description": "Check if a file exists in the mod"
    },
    "Start New Level": {
        "category": "Game Control",
        "code": "StartLevel(\"level_name\")",
        "description": "Load and start a new level"
    },
    "Get Frame Time Step": {
        "category": "Game Control",
        "code": "local dt = GetTimeStep()",
        "description": "Get timestep of the last frame (60 updates/sec in update, actual time in tick/draw)"
    },


    #input
    "Get Last Key Pressed": {
        "category": "Input",
        "code": "local key = InputLastPressedKey(playerId)",
        "description": "Get the name of the last key that was pressed"
    },
    "Check if Key was Released": {
        "category": "Input",
        "code": 'if InputReleased("jump") then\n    -- Jump key was released this frame\nend',
        "description": "Check if a key was released this frame"
    },
    "Get Analog Input Value": {
        "category": "Input",
        "code": 'local value = InputValue("mousewheel")',
        "description": "Get analog value from input (like mouse wheel or joystick)"
    },
    "Clear All Input": {
        "category": "Input",
        "code": "InputClear()",
        "description": "Clear all stored input for this frame"
    },
    "Reset Input on State Change": {
        "category": "Input",
        "code": "InputResetOnTransition()",
        "description": "Reset input when changing states (client only)"
    },
    "Get Last Input Device": {
        "category": "Input",
        "code": "local device = LastInputDevice()",
        "description": "Get which input device was used last (0=none, 1=mouse, 2=gamepad)"
    },
    "Check if Key was Pressed": {
        "category": "Input",
        "code": 'if InputPressed("jump") then\n    -- Jump key was pressed this frame\nend',
        "description": "Check if a key was pressed this frame"
    },
    "Check if Key is Held": {
        "category": "Input",
        "code": 'if InputDown("forward") then\n    -- Forward key is being held\nend',
        "description": "Check if a key is currently being held down"
    },
    "Get the Mouse Movement": {
        "category": "Input",
        "code": "local mouse_x = InputValue(\"mousedx\")\nlocal mouse_y = InputValue(\"mousedy\")",
        "description": "Get mouse movement since last frame"
    },
    "Get Mouse Wheel": {
        "category": "Input",
        "code": "local wheel = InputValue(\"mousewheel\")",
        "description": "Get mouse wheel movement"
    },
    "Get Camera Movement": {
        "category": "Input",
        "code": "local cam_x = InputValue(\"camerax\")\nlocal cam_y = InputValue(\"cameray\")",
        "description": "Get camera movement (scaled by sensitivity)"
    },
    "Switch Tool Group Previous": {
        "category": "Input",
        "code": "if InputPressed(\"tool_group_prev\") then\n    -- Previous tool group\nend",
        "description": "Switch to previous tool group"
    },
    "Switch Tool Group Next": {
        "category": "Input",
        "code": "if InputPressed(\"tool_group_next\") then\n    -- Next tool group\nend",
        "description": "Switch to next tool group"
    },
    "Raise Vehicle Parts": {
        "category": "Input",
        "code": "if InputPressed(\"vehicleraise\") then\n    -- Raise vehicle parts\nend",
        "description": "Raise vehicle parts"
    },
    "Lower Vehicle Parts": {
        "category": "Input",
        "code": "if InputPressed(\"vehiclelower\") then\n    -- Lower vehicle parts\nend",
        "description": "Lower vehicle parts"
    },
    "Vehicle Action": {
        "category": "Input",
        "code": "if InputPressed(\"vehicleaction\") then\n    -- Vehicle action\nend",
        "description": "Perform vehicle action"
    },
    "Extra Action 0": {
        "category": "Input",
        "code": "if InputPressed(\"extra0\") then\n    -- Extra action 0\nend",
        "description": "Extra action 0"
    },
    "Check Input Device (Gamepad)": {
        "category": "Input",
        "code": "if LastInputDevice() == UI_DEVICE_GAMEPAD then\n    -- Gamepad input\nend",
        "description": "Check if last input was from gamepad"
    },
    "Check Input Device (Mouse)": {
        "category": "Input",
        "code": "if LastInputDevice() == UI_DEVICE_MOUSE then\n    -- Mouse input\nend",
        "description": "Check if last input was from mouse"
    },
    "Check Input Device (Touch)": {
        "category": "Input",
        "code": "if LastInputDevice() == UI_DEVICE_TOUCHSCREEN then\n    -- Touchscreen input\nend",
        "description": "Check if last input was from touchscreen"
    },
    "Get Last Input Device": {
        "category": "Input",
        "code": "local device = LastInputDevice()",
        "description": "Get the type of the last input device (gamepad, mouse, touchscreen)"
    },
    "Reset Input on State Change": {
        "category": "Input",
        "code": "InputResetOnTransition()",
        "description": "Reset input detection when changing game states (prevents stuck inputs)"
    },


    #data storage
    "Delete a Registry Key": {
        "category": "Data Storage",
        "code": 'ClearKey("my_key")',
        "description": "Delete a key and all its child keys from storage"
    },
    "List All Keys": {
        "category": "Data Storage",
        "code": 'local keys = ListKeys("parent_key")',
        "description": "Get a list of all child keys under a parent key"
    },
    "Check if Key Exists": {
        "category": "Data Storage",
        "code": 'if HasKey("my_key") then\n    -- Key exists in storage\nend',
        "description": "Check if a key exists in the registry storage"
    },
    "Save a True/False Value": {
        "category": "Data Storage",
        "code": 'SetBool("my_setting", true, sync_to_clients)',
        "description": "Save a boolean value to persistent storage (optional sync to clients)"
    },
    "Load a True/False Value": {
        "category": "Data Storage",
        "code": 'local enabled = GetBool("my_setting")',
        "description": "Load a boolean value from persistent storage"
    },
    "Save a Decimal Value": {
        "category": "Data Storage",
        "code": 'SetFloat("my_value", 3.14, sync_to_clients)',
        "description": "Save a decimal number to persistent storage (optional sync to clients)"
    },
    "Load a Decimal Value": {
        "category": "Data Storage",
        "code": 'local value = GetFloat("my_value")',
        "description": "Load a decimal number from persistent storage"
    },
    "Save a Number Value": {
        "category": "Data Storage",
        "code": 'SetInt("my_score", 100, sync_to_clients)',
        "description": "Save a number value to persistent storage (optional sync to clients)"
    },
    "Load a Number Value": {
        "category": "Data Storage",
        "code": 'local score = GetInt("my_score")',
        "description": "Load a number value from persistent storage"
    },
    "Save a Text Value": {
        "category": "Data Storage", 
        "code": 'SetString("player_name", "John", sync_to_clients)',
        "description": "Save a text value to persistent storage (optional sync to clients)"
    },
    "Load a Text Value": {
        "category": "Data Storage",
        "code": 'local name = GetString("player_name")',
        "description": "Load a text value from persistent storage"
    },
    "Save a Color Value": {
        "category": "Data Storage",
        "code": "SetColor(\"my_color\", r, g, b, a)",
        "description": "Save a color value to persistent storage (RGBA)"
    },
    "Load a Color Value": {
        "category": "Data Storage",
        "code": "local r, g, b, a = GetColor(\"my_color\")",
        "description": "Load a color value from persistent storage (RGBA)"
    },
    "Use Shared Data Table": {
        "category": "Data Storage",
        "code": "shared.gameScore = 100\nshared.playerNames = {\"Alice\", \"Bob\"}",
        "description": "Store data that automatically syncs from server to all clients"
    },
    "Read Shared Data": {
        "category": "Data Storage",
        "code": "local score = shared.gameScore\nlocal players = shared.playerNames",
        "description": "Read shared data (read-only on clients, writable on server)"
    },
    "Sync Registry to Clients": {
        "category": "Data Storage",
        "code": 'SetInt("global.score", 100, true)\nSetBool("game.started", true, true)',
        "description": "Save registry values and sync them to all clients"
    },
    "Set Value in Table": {
        "category": "Data Storage",
        "code": "SetValueInTable(my_table, \"key\", value, \"number\", 1)",
        "description": "Set a value in a specific table with type and length limit"
    },


    #math
    "Get Vector Length": {
        "category": "Math",
        "code": "local length = VecLength(vector)",
        "description": "Get the length (magnitude) of a vector"
    },
    "Normalize Vector": {
        "category": "Math",
        "code": "local normalized = VecNormalize(vector)",
        "description": "Create a normalized vector of length 1.0"
    },
    "Scale Vector": {
        "category": "Math",
        "code": "local scaled = VecScale(vector, scale_factor)",
        "description": "Multiply a vector by a scale factor"
    },
    "Subtract Vectors": {
        "category": "Math",
        "code": "local result = VecSub(vec1, vec2)",
        "description": "Subtract one vector from another (vec1 - vec2)"
    },
    "Get Dot Product": {
        "category": "Math",
        "code": "local dot = VecDot(vec1, vec2)",
        "description": "Calculate the dot product of two vectors"
    },
    "Get Cross Product": {
        "category": "Math",
        "code": "local cross = VecCross(vec1, vec2)",
        "description": "Calculate the cross product of two vectors"
    },
    "Mix Vectors": {
        "category": "Math",
        "code": "local mixed = VecLerp(vec1, vec2, t)",
        "description": "Mix between two vectors using a factor (0.0 to 1.0)"
    },
    "Make a Rotation": {
        "category": "Math",
        "code": "local quat = Quat(x, y, z, w)",
        "description": "Create a quaternion for rotations"
    },
    "Copy a Rotation": {
        "category": "Math",
        "code": "local copy = QuatCopy(quaternion)",
        "description": "Create a copy of a quaternion"
    },
    "Make a Rotation from Axis": {
        "category": "Math",
        "code": "local quat = QuatAxisAngle(axis_vector, angle_in_radians)",
        "description": "Create a rotation quaternion from axis and angle"
    },
    "Create Rotation from Normals": {
        "category": "Math",
        "code": "local quat = QuatDeltaNormals(normal1, normal2)",
        "description": "Create rotation between two normal vectors"
    },
    "Create Rotation from Vectors": {
        "category": "Math",
        "code": "local quat = QuatDeltaVectors(vec1, vec2)",
        "description": "Create rotation between any two vectors"
    },
    "Create Rotation from Angles": {
        "category": "Math",
        "code": "local quat = QuatEuler(pitch, yaw, roll)",
        "description": "Create quaternion from Euler angles (pitch, yaw, roll)"
    },
    "Align Rotation to Axes": {
        "category": "Math",
        "code": "local aligned = QuatAlignXZ(quaternion)",
        "description": "Align quaternion to XZ axes"
    },
    "Get Rotation Angles": {
        "category": "Math",
        "code": "local pitch, yaw, roll = GetQuatEuler(quaternion)",
        "description": "Get Euler angles from a quaternion"
    },
    "Make Rotation Look at Point": {
        "category": "Math",
        "code": "local quat = QuatLookAt(from_position, to_position)",
        "description": "Create rotation to look at a point (useful for cameras)"
    },
    "Mix Rotations": {
        "category": "Math",
        "code": "local mixed = QuatSlerp(quat1, quat2, t)",
        "description": "Smoothly mix between two rotations"
    },
    "Convert Rotation to Text": {
        "category": "Math",
        "code": "local text = QuatStr(quaternion)",
        "description": "Convert quaternion to string representation"
    },
    "Combine Rotations": {
        "category": "Math",
        "code": "local result = QuatRotateQuat(quat1, quat2)",
        "description": "Combine two rotations (multiply quaternions)"
    },
    "Rotate a Vector": {
        "category": "Math",
        "code": "local rotated = QuatRotateVec(quaternion, vector)",
        "description": "Rotate a vector by a quaternion"
    },
    "Create a Transform": {
        "category": "Math",
        "code": "local transform = Transform(position, rotation)",
        "description": "Create a transform with position and rotation"
    },
    "Copy a Transform": {
        "category": "Math",
        "code": "local copy = TransformCopy(transform)",
        "description": "Create a copy of a transform (prevents reference issues)"
    },
    "Convert Transform to Text": {
        "category": "Math",
        "code": "local text = TransformStr(transform)",
        "description": "Convert transform to string representation"
    },
    "Transform to Parent Space": {
        "category": "Math",
        "code": "local parent_transform = TransformToParentTransform(child_transform, parent)",
        "description": "Convert transform from local to parent space"
    },
    "Transform to Local Space": {
        "category": "Math",
        "code": "local local_transform = TransformToLocalTransform(transform, parent)",
        "description": "Convert transform from parent to local space"
    },
    "Transform Vector to Parent": {
        "category": "Math",
        "code": "local parent_vec = TransformToParentVec(vector, transform)",
        "description": "Transform vector from local to parent space (rotation only)"
    },
    "Transform Vector to Local": {
        "category": "Math",
        "code": "local local_vec = TransformToLocalVec(vector, transform)",
        "description": "Transform vector from parent to local space (rotation only)"
    },
    "Transform Point to Parent": {
        "category": "Math",
        "code": "local parent_point = TransformToParentPoint(point, transform)",
        "description": "Transform point from local to world space"
    },
    "Transform Point to Local": {
        "category": "Math",
        "code": "local local_point = TransformToLocalPoint(point, transform)",
        "description": "Transform point from world to local space"
    },
    "Generate Random Boolean": {
        "category": "Math",
        "code": "local result = GetRandomBool()",
        "description": "Generate random true/false value"
    },
    "Generate Random Direction": {
        "category": "Math",
        "code": "local direction = GetRandomDirection()",
        "description": "Generate random direction vector"
    },
    "Set Random Seed": {
        "category": "Math",
        "code": "SetRandomSeed(seed_value)",
        "description": "Set seed for random number generation"
    },
    "Create a Position Vector": {
        "category": "Math",
        "code": 'local pos = Vec(x, y, z)',
        "description": "Create a 3D position vector"
    },
    "Copy a Vector": {
        "category": "Math",
        "code": "local copy = VecCopy(vector)",
        "description": "Create a copy of a vector (prevents reference issues)"
    },
    "Convert Vector to Text": {
        "category": "Math",
        "code": "local text = VecStr(vector)",
        "description": "Convert a vector to a string representation"
    },
    "Add Vectors": {
        "category": "Math",
        "code": 'local result = VecAdd(vec1, vec2)',
        "description": "Add two vectors together"
    },
    "Get a Random Number": {
        "category": "Math",
        "code": 'local random_num = GetRandomFloat(min, max)',
        "description": "Get a random floating point number"
    },
    "Get a Random Integer": {
        "category": "Math", 
        "code": 'local random_int = GetRandomInt(min, max)',
        "description": "Get a random integer"
    },


    #bodies
    "Find a Physics Body": {
        "category": "Bodies",
        "code": 'local body = FindBody("body_name")',
        "description": "Find a physics body by its tag name"
    },
    "Find All Physics Bodies": {
        "category": "Bodies",
        "code": 'local bodies = FindBodies("body_name")',
        "description": "Find all physics bodies with a specific tag"
    },
    "Get a Body's Position": {
        "category": "Bodies",
        "code": "local transform = GetBodyTransform(body)",
        "description": "Get the position and rotation of a physics body"
    },
    "Set a Body's Position": {
        "category": "Bodies",
        "code": "SetBodyTransform(body, transform)",
        "description": "Set the position and rotation of a physics body"
    },
    "Get a Body's Mass": {
        "category": "Bodies",
        "code": "local mass = GetBodyMass(body)",
        "description": "Get the mass of a physics body"
    },
    "Check if a Body Moves": {
        "category": "Bodies",
        "code": "if IsBodyDynamic(body) then\n    -- Body is affected by physics\nend",
        "description": "Check if a body is dynamic (moves) or static"
    },
    "Make a Body Move": {
        "category": "Bodies",
        "code": "SetBodyDynamic(body, true)",
        "description": "Make a static body become dynamic (affected by physics)"
    },
    "Get a Body's Speed": {
        "category": "Bodies",
        "code": "local velocity = GetBodyVelocity(body)",
        "description": "Get the current velocity of a physics body"
    },
    "Get Body Speed at Position": {
        "category": "Bodies",
        "code": "local velocity = GetBodyVelocityAtPos(body, position)",
        "description": "Get velocity at a specific point on a body"
    },
    "Get a Body's Rotation Speed": {
        "category": "Bodies",
        "code": "local angular_vel = GetBodyAngularVelocity(body)",
        "description": "Get the rotation speed of a physics body"
    },
    "Set a Body's Rotation Speed": {
        "category": "Bodies",
        "code": "SetBodyAngularVelocity(body, angular_velocity)",
        "description": "Set the rotation speed of a physics body"
    },
    "Check if Body is Active": {
        "category": "Bodies",
        "code": "if IsBodyActive(body) then\n    -- Body is being simulated\nend",
        "description": "Check if a body is currently being simulated"
    },
    "Set Body Active State": {
        "category": "Bodies",
        "code": "SetBodyActive(body, true)",
        "description": "Manually activate or deactivate a body in simulation"
    },
    "Get Body's Shapes": {
        "category": "Bodies",
        "code": "local shapes = GetBodyShapes(body)",
        "description": "Get all shapes owned by a body"
    },
    "Get Body's Vehicle": {
        "category": "Bodies",
        "code": "local vehicle = GetBodyVehicle(body)",
        "description": "Get the vehicle that owns this body"
    },
    "Get Body's Bounds": {
        "category": "Bodies",
        "code": "local min, max = GetBodyBounds(body)",
        "description": "Get the bounding box of a body"
    },
    "Get Body's Center of Mass": {
        "category": "Bodies",
        "code": "local center = GetBodyCenterOfMass(body)",
        "description": "Get the center of mass of a body"
    },
    "Get Body's Animator": {
        "category": "Bodies",
        "code": "local animator = GetBodyAnimator(body)",
        "description": "Get the animator handle for a body"
    },
    "Get Body's Player": {
        "category": "Bodies",
        "code": "local player = GetBodyPlayer(body)",
        "description": "Get the player who owns this body"
    },
    "Check if Body is Visible": {
        "category": "Bodies",
        "code": "if IsBodyVisible(body) then\n    -- Body is visible to camera\nend",
        "description": "Check if a body is visible to the camera"
    },
    "Check if Body is Broken": {
        "category": "Bodies",
        "code": "if IsBodyBroken(body) then\n    -- Body has been damaged\nend",
        "description": "Check if any part of a body has been broken"
    },
    "Check if Body is Connected to Static": {
        "category": "Bodies",
        "code": "if IsBodyJointedToStatic(body) then\n    -- Body is connected to static object\nend",
        "description": "Check if a body is connected to something static"
    },
    "Draw Body Outline": {
        "category": "Bodies",
        "code": "DrawBodyOutline(body)",
        "description": "Draw an outline around a body for one frame"
    },
    "Highlight Body": {
        "category": "Bodies",
        "code": "DrawBodyHighlight(body)",
        "description": "Flash/highlight a body for one frame"
    },
    "Constrain Body Velocity": {
        "category": "Bodies",
        "code": "ConstrainVelocity(body, target_velocity, max_angular)",
        "description": "Constrain body velocity (use in update callback)"
    },
    "Constrain Body Angular Velocity": {
        "category": "Bodies",
        "code": "ConstrainAngularVelocity(body, target_angular, max_angular)",
        "description": "Constrain body rotation speed (use in update callback)"
    },
    "Get a Body's Closest Point": {
        "category": "Bodies",
        "code": "local point, hit, normal, shape = GetBodyClosestPoint(body, position)",
        "description": "Find the closest point on a body to a given position"
    },
    "Constrain a Body's Position": {
        "category": "Bodies",
        "code": "ConstrainPosition(body, target_position, max_distance)",
        "description": "Physically move a body towards a target position"
    },
    "Constrain a Body's Rotation": {
        "category": "Bodies",
        "code": "ConstrainOrientation(body, target_rotation, max_speed)",
        "description": "Physically rotate a body towards a target rotation"
    },
    "Get the World Body": {
        "category": "Bodies",
        "code": "local world_body = GetWorldBody()",
        "description": "Get the static world body (contains all unassigned shapes)"
    },


    #shapes
    "Find a Shape": {
        "category": "Shapes",
        "code": 'local shape = FindShape("shape_name")',
        "description": "Find a voxel shape by its tag name"
    },
    "Find All Shapes": {
        "category": "Shapes",
        "code": 'local shapes = FindShapes("shape_name")',
        "description": "Find all voxel shapes with a specific tag"
    },
    "Get a Shape's Position": {
        "category": "Shapes",
        "code": "local transform = GetShapeLocalTransform(shape)",
        "description": "Get the position of a shape relative to its parent body"
    },
    "Set a Shape's Position": {
        "category": "Shapes",
        "code": "SetShapeLocalTransform(shape, transform)",
        "description": "Set the position of a shape relative to its parent body"
    },
    "Get a Shape's World Position": {
        "category": "Shapes",
        "code": "local transform = GetShapeWorldTransform(shape)",
        "description": "Get the world position of a shape"
    },
    "Get a Shape's Body": {
        "category": "Shapes",
        "code": "local body = GetShapeBody(shape)",
        "description": "Get the physics body that owns this shape"
    },
    "Get Shape's Joints": {
        "category": "Shapes",
        "code": "local joints = GetShapeJoints(shape)",
        "description": "Get all joints connected to a shape"
    },
    "Get Shape's Lights": {
        "category": "Shapes",
        "code": "local lights = GetShapeLights(shape)",
        "description": "Get all lights owned by a shape"
    },
    "Get Shape's Bounds": {
        "category": "Shapes",
        "code": "local min, max = GetShapeBounds(shape)",
        "description": "Get the bounding box of a shape"
    },
    "Set Shape Brightness": {
        "category": "Shapes",
        "code": "SetShapeEmissiveScale(shape, brightness)",
        "description": "Set how bright a shape glows"
    },
    "Set Shape Density": {
        "category": "Shapes",
        "code": "SetShapeDensity(shape, density_value)",
        "description": "Change the material density of a shape"
    },
    "Get Shape Size": {
        "category": "Shapes",
        "code": "local size = GetShapeSize(shape)",
        "description": "Get the dimensions of a shape in voxels"
    },
    "Count Shape Voxels": {
        "category": "Shapes",
        "code": "local count = GetShapeVoxelCount(shape)",
        "description": "Count how many voxels are in a shape"
    },
    "Check if Shape is Visible": {
        "category": "Shapes",
        "code": "if IsShapeVisible(shape) then\n    -- Shape is visible to camera\nend",
        "description": "Check if a shape is visible to the camera"
    },
    "Check if Shape is Broken": {
        "category": "Shapes",
        "code": "if IsShapeBroken(shape) then\n    -- Shape has been damaged\nend",
        "description": "Check if a shape has been broken"
    },
    "Set Shape Collision Layers": {
        "category": "Shapes",
        "code": "SetShapeCollisionFilter(shape, filter_mask)",
        "description": "Set which collision layers a shape uses"
    },
    "Get Shape Collision Layers": {
        "category": "Shapes",
        "code": "local filter = GetShapeCollisionFilter(shape)",
        "description": "Get the collision layer settings of a shape"
    },
    "Move Shape to Body": {
        "category": "Shapes",
        "code": "SetShapeBody(shape, new_body)",
        "description": "Move a shape to a different physics body"
    },
    "Copy Shape Content": {
        "category": "Shapes",
        "code": "CopyShapeContent(source_shape, target_shape)",
        "description": "Copy voxels from one shape to another"
    },
    "Copy Shape Palette": {
        "category": "Shapes",
        "code": "CopyShapePalette(source_shape, target_shape)",
        "description": "Copy material palette from one shape to another"
    },
    "Get Shape Palette": {
        "category": "Shapes",
        "code": "local palette = GetShapePalette(shape)",
        "description": "Get all material entries in a shape's palette"
    },
    "Extrude Shape": {
        "category": "Shapes",
        "code": "ExtrudeShape(shape, direction, distance)",
        "description": "Extrude/pull out part of a shape"
    },
    "Trim Shape": {
        "category": "Shapes",
        "code": "TrimShape(shape, cutting_plane)",
        "description": "Cut away empty parts of a shape"
    },
    "Split Shape": {
        "category": "Shapes",
        "code": "local shape1, shape2 = SplitShape(shape, cutting_plane)",
        "description": "Split a shape into multiple parts"
    },
    "Merge Shapes": {
        "category": "Shapes",
        "code": "local merged = MergeShape(shapes_list)",
        "description": "Try to merge touching shapes together"
    },
    "Check if Shape is Disconnected": {
        "category": "Shapes",
        "code": "if IsShapeDisconnected(shape) then\n    -- Shape has detached parts\nend",
        "description": "Check if a shape has disconnected parts"
    },
    "Check if Static Shape is Detached": {
        "category": "Shapes",
        "code": "if IsStaticShapeDetached(shape) then\n    -- Static shape has detached parts\nend",
        "description": "Check if a static shape has detached parts"
    },
    "Get Closest Point on Shape": {
        "category": "Shapes",
        "code": "local point, hit, normal = GetShapeClosestPoint(shape, position)",
        "description": "Find the closest point on a shape to a position"
    },
    "Check if Shapes Touch": {
        "category": "Shapes",
        "code": "if IsShapeTouching(shape1, shape2) then\n    -- Shapes are overlapping\nend",
        "description": "Check if two shapes are touching/overlapping"
    },
    "Create a New Shape": {
        "category": "Shapes",
        "code": "local new_shape = CreateShape(material, size)",
        "description": "Create a new voxel shape with specified material and size"
    },
    "Clear a Shape": {
        "category": "Shapes",
        "code": "ClearShape(shape)",
        "description": "Remove all voxels from a shape"
    },
    "Resize a Shape": {
        "category": "Shapes",
        "code": "ResizeShape(shape, new_size)",
        "description": "Resize a shape to new dimensions"
    },
    "Draw a Line on Shape": {
        "category": "Shapes",
        "code": "DrawShapeLine(shape, start_pos, end_pos, material)",
        "description": "Draw a line of voxels on a shape"
    },
    "Draw a Box on Shape": {
        "category": "Shapes",
        "code": "DrawShapeBox(shape, min_pos, max_pos, material)",
        "description": "Draw a filled box of voxels on a shape"
    },


    #vehicles
    "Find All Vehicles": {
        "category": "Vehicles",
        "code": 'local vehicles = FindVehicles("vehicle_name")',
        "description": "Find all vehicles with a specific tag"
    },
    "Get a Vehicle's Position": {
        "category": "Vehicles",
        "code": "local transform = GetVehicleTransform(vehicle)",
        "description": "Get the position and rotation of a vehicle"
    },
    "Get a Vehicle's Exhaust Positions": {
        "category": "Vehicles",
        "code": "local exhausts = GetVehicleExhaustTransforms(vehicle)",
        "description": "Get positions of vehicle exhaust pipes"
    },
    "Get a Vehicle's Important Parts": {
        "category": "Vehicles",
        "code": "local vitals = GetVehicleVitalTransforms(vehicle)",
        "description": "Get positions of important vehicle parts"
    },
    "Get a Vehicle's Bodies": {
        "category": "Vehicles",
        "code": "local bodies = GetVehicleBodies(vehicle)",
        "description": "Get all physics bodies that make up a vehicle"
    },
    "Get a Vehicle's Body": {
        "category": "Vehicles",
        "code": "local body = GetVehicleBody(vehicle, body_name)",
        "description": "Get a specific body from a vehicle"
    },
    "Get Vehicle's Parameters": {
        "category": "Vehicles",
        "code": "local params = GetVehicleParams(vehicle)",
        "description": "Get all vehicle parameters (speed, acceleration, etc.)"
    },
    "Set Vehicle Parameter": {
        "category": "Vehicles",
        "code": "SetVehicleParam(vehicle, \"parameter_name\", value)",
        "description": "Set a specific vehicle parameter"
    },
    "Get Driver's Position": {
        "category": "Vehicles",
        "code": "local pos = GetVehicleDriverPos(vehicle)",
        "description": "Get the driver's position relative to vehicle"
    },
    "Get Available Seat Position": {
        "category": "Vehicles",
        "code": "local seat_pos = GetVehicleAvailableSeatPos(vehicle)",
        "description": "Get the next available seat position"
    },
    "Get Vehicle Steering": {
        "category": "Vehicles",
        "code": "local steering = GetVehicleSteering(vehicle)",
        "description": "Get how much the vehicle is turning (-1 to 1)"
    },
    "Get Vehicle Throttle": {
        "category": "Vehicles",
        "code": "local throttle = GetVehicleDrive(vehicle)",
        "description": "Get how much gas/brake is being applied (-1 to 1)"
    },
    "Get Vehicle Location Transform": {
        "category": "Vehicles",
        "code": "local transform = GetVehicleLocationWorldTransform(vehicle)",
        "description": "Get the world position of a vehicle location"
    },
    "Get Vehicle Passenger Info": {
        "category": "Vehicles",
        "code": "local passengers, seats, has_driver = GetVehiclePassengerCount(vehicle)",
        "description": "Get passenger count and seat availability"
    },
    "Find a Vehicle": {
        "category": "Vehicles",
        "code": 'local vehicle = FindVehicle("vehicle_name")',
        "description": "Find a vehicle in the scene"
    },
    "Get a Vehicle's Health": {
        "category": "Vehicles",
        "code": "local health = GetVehicleHealth(vehicle)",
        "description": "Get the health percentage of a vehicle"
    },
    "Set a Vehicle's Health": {
        "category": "Vehicles",
        "code": "SetVehicleHealth(vehicle, health)",
        "description": "Set the health percentage of a vehicle"
    },
    "Drive a Vehicle": {
        "category": "Vehicles",
        "code": "DriveVehicle(vehicle, steering, throttle, brake)",
        "description": "Control a vehicle's movement"
    },


    #rigs
    "Find a Rig": {
        "category": "Rigs",
        "code": 'local rig = FindRig("rig_name")',
        "description": "Find a rig (skeleton) by its tag name"
    },
    "Get Rig's World Position": {
        "category": "Rigs",
        "code": "local transform = GetRigWorldTransform(rig)",
        "description": "Get the world position of a rig"
    },
    "Set Rig's World Position": {
        "category": "Rigs",
        "code": "SetRigWorldTransform(rig, transform)",
        "description": "Set the world position of a rig"
    },
    "Get Rig Location World Position": {
        "category": "Rigs",
        "code": "local transform = GetRigLocationWorldTransform(rig, \"location_name\")",
        "description": "Get the world position of a rig location"
    },
    "Set Rig Location World Position": {
        "category": "Rigs",
        "code": "SetRigLocationWorldTransform(rig, \"location_name\", transform)",
        "description": "Set the world position of a rig location"
    },
    "Get Rig Location Local Position": {
        "category": "Rigs",
        "code": "local transform = GetRigLocationLocalTransform(rig, \"location_name\")",
        "description": "Get the local position of a rig location"
    },
    "Set Rig Location Local Position": {
        "category": "Rigs",
        "code": "SetRigLocationLocalTransform(rig, \"location_name\", transform)",
        "description": "Set the local position of a rig location"
    },


    #joints
    "Find a Joint": {
        "category": "Joints",
        "code": 'local joint = FindJoint("joint_name")',
        "description": "Find a physical joint by its tag name"
    },
    "Find All Joints": {
        "category": "Joints",
        "code": 'local joints = FindJoints("joint_name")',
        "description": "Find all physical joints with a specific tag"
    },
    "Get Joint Type": {
        "category": "Joints",
        "code": "local type = GetJointType(joint)",
        "description": "Get the type of joint (ball, hinge, or prismatic)"
    },
    "Get Joint's Other Shape": {
        "category": "Joints",
        "code": "local other_shape = GetJointOtherShape(joint, shape)",
        "description": "Get the other shape a joint is connected to"
    },
    "Get Joint's Shapes": {
        "category": "Joints",
        "code": "local shapes = GetJointShapes(joint)",
        "description": "Get both shapes that a joint is connected to"
    },
    "Set Joint Motor Speed": {
        "category": "Joints",
        "code": "SetJointMotor(joint, speed, torque)",
        "description": "Set a joint's motor speed and torque"
    },
    "Set Joint Motor Target": {
        "category": "Joints",
        "code": "SetJointMotorTarget(joint, target, speed, torque)",
        "description": "Make a joint move to a specific position"
    },
    "Get Joint Movement Limits": {
        "category": "Joints",
        "code": "local min_limit, max_limit = GetJointLimits(joint)",
        "description": "Get the movement limits of a joint"
    },
    "Get Joint Current Position": {
        "category": "Joints",
        "code": "local position = GetJointMovement(joint)",
        "description": "Get the current position/angle of a joint"
    },
    "Get All Jointed Bodies": {
        "category": "Joints",
        "code": "local bodies = GetJointedBodies(body)",
        "description": "Get all bodies connected to a body via joints"
    },
    "Detach Joint from Shape": {
        "category": "Joints",
        "code": "DetachJointFromShape(joint, shape)",
        "description": "Detach a joint from a specific shape"
    },
    "Check if a Joint is Broken": {
        "category": "Joints",
        "code": "if IsJointBroken(joint) then\n    -- Joint has been broken\nend",
        "description": "Check if a joint has been broken by damage"
    },


    #ropes
    "Get Number of Rope Points": {
        "category": "Ropes",
        "code": "local count = GetRopeNumberOfPoints(rope)",
        "description": "Get how many points a rope has"
    },
    "Get Rope Point Position": {
        "category": "Ropes",
        "code": "local pos = GetRopePointPosition(rope, point_index)",
        "description": "Get the world position of a specific rope point"
    },
    "Get a Rope's Bounds": {
        "category": "Ropes",
        "code": "local bounds = GetRopeBounds(rope)",
        "description": "Get the bounding box of a rope"
    },
    "Break a Rope": {
        "category": "Ropes",
        "code": "BreakRope(rope)",
        "description": "Break a rope at its current position"
    },


    #animation
    "Set Bone Position": {
        "category": "Animation",
        "code": "SetAnimatorPositionIK(animator, target_position, bone_name)",
        "description": "Make a bone reach for a target position"
    },
    "Set Bone Transform": {
        "category": "Animation",
        "code": "SetAnimatorTransformIK(animator, target_transform, bone_name)",
        "description": "Make a bone reach for a target transform"
    },
    "Get Bone Chain Length": {
        "category": "Animation",
        "code": "local length = GetBoneChainLength(animator, bone_name)",
        "description": "Get the length of a bone chain"
    },
    "Find an Animator": {
        "category": "Animation",
        "code": 'local animator = FindAnimator("animator_name")',
        "description": "Find an animator by its tag name"
    },
    "Find All Animators": {
        "category": "Animation",
        "code": 'local animators = FindAnimators("animator_name")',
        "description": "Find all animators with a specific tag"
    },
    "Get Animator Position": {
        "category": "Animation",
        "code": "local transform = GetAnimatorTransform(animator)",
        "description": "Get the world position of an animator"
    },
    "Set Animator Position": {
        "category": "Animation",
        "code": "SetAnimatorTransform(animator, transform)",
        "description": "Set the world position of an animator"
    },
    "Get IK Target Adjustment": {
        "category": "Animation",
        "code": "local transform = GetAnimatorAdjustTransformIK(animator)",
        "description": "Get the adjusted target transform for IK system"
    },
    "Stop Being a Ragdoll": {
        "category": "Animation",
        "code": "UnRagdoll(animator)",
        "description": "Convert a ragdoll back to animated character"
    },
    "Play Animation Instance": {
        "category": "Animation",
        "code": "local instance = PlayAnimationInstance(animator, \"animation_name\")",
        "description": "Play an animation and get its instance handle"
    },
    "Stop Animation Instance": {
        "category": "Animation",
        "code": "StopAnimationInstance(instance)",
        "description": "Stop a specific animation instance"
    },
    "Play Animation at Frame": {
        "category": "Animation",
        "code": "PlayAnimationFrame(animator, \"animation_name\", frame_number)",
        "description": "Play an animation starting at a specific frame"
    },
    "Start Animation Blend Group": {
        "category": "Animation",
        "code": "BeginAnimationGroup()",
        "description": "Start a group for blending multiple animations"
    },
    "End Animation Blend Group": {
        "category": "Animation",
        "code": "EndAnimationGroup()",
        "description": "End an animation blend group"
    },
    "Process Animation Instances": {
        "category": "Animation",
        "code": "PlayAnimationInstances()",
        "description": "Force animation instances to be processed"
    },
    "Get All Animation Names": {
        "category": "Animation",
        "code": "local names = GetAnimationClipNames(animator)",
        "description": "Get all available animation names"
    },
    "Get Animation Duration": {
        "category": "Animation",
        "code": "local duration = GetAnimationClipDuration(animator, \"animation_name\")",
        "description": "Get the length of an animation in seconds"
    },
    "Set Animation Fade Times": {
        "category": "Animation",
        "code": "SetAnimationClipFade(animator, \"animation_name\", fade_in, fade_out)",
        "description": "Set fade in and fade out times for an animation"
    },
    "Set Animation Speed": {
        "category": "Animation",
        "code": "SetAnimationClipSpeed(animator, \"animation_name\", speed_multiplier)",
        "description": "Change the playback speed of an animation"
    },
    "Trim Animation": {
        "category": "Animation",
        "code": "TrimAnimationClip(animator, \"animation_name\", start_time, length)",
        "description": "Trim an animation to specific start and length"
    },
    "Get Animation Current Time": {
        "category": "Animation",
        "code": "local time = GetAnimationClipLoopPosition(animator, \"animation_name\")",
        "description": "Get current playback position of an animation"
    },
    "Get Instance Current Time": {
        "category": "Animation",
        "code": "local time = GetAnimationInstancePosition(instance)",
        "description": "Get current playback position of an animation instance"
    },
    "Set Animation Current Time": {
        "category": "Animation",
        "code": "SetAnimationClipLoopPosition(animator, \"animation_name\", time)",
        "description": "Set current playback position of an animation"
    },
    "Set Bone Rotation": {
        "category": "Animation",
        "code": "SetBoneRotation(animator, \"bone_name\", rotation_quat)",
        "description": "Set the rotation of a specific bone"
    },
    "Make Bone Look at Point": {
        "category": "Animation",
        "code": "SetBoneLookAt(animator, \"bone_name\", target_position)",
        "description": "Make a bone point at a specific world position"
    },
    "Rotate Bone": {
        "category": "Animation",
        "code": "RotateBone(animator, \"bone_name\", rotation_quat)",
        "description": "Add rotation to a bone"
    },
    "Get All Bone Names": {
        "category": "Animation",
        "code": "local bones = GetBoneNames(animator)",
        "description": "Get all bone names in an animator"
    },
    "Get Bone's Body": {
        "category": "Animation",
        "code": "local body = GetBoneBody(animator, \"bone_name\")",
        "description": "Get the physics body attached to a bone"
    },
    "Get Bone World Position": {
        "category": "Animation",
        "code": "local transform = GetBoneWorldTransform(animator, \"bone_name\")",
        "description": "Get the world position of a bone"
    },
    "Get Bone Default Position": {
        "category": "Animation",
        "code": "local transform = GetBoneBindPoseTransform(animator, \"bone_name\")",
        "description": "Get the default position of a bone"
    },
    "Play an Animation": {
        "category": "Animation",
        "code": 'PlayAnimation(animator, "animation_name")',
        "description": "Play a one-time animation on an animator"
    },
    "Play a Looping Animation": {
        "category": "Animation",
        "code": 'PlayAnimationLoop(animator, "animation_name")',
        "description": "Play a looping animation (must be called every frame)"
    },
    "Make a Ragdoll": {
        "category": "Animation",
        "code": "MakeRagdoll(animator)",
        "description": "Convert an animated character to a physics ragdoll"
    },
}

def get_categories():
    """Get all unique categories from the function definitions"""
    return sorted(set(func["category"] for func in TEARDOWN_FUNCTIONS.values()))

def get_functions_by_category(category):
    """Get all functions in a specific category"""
    return {name: func for name, func in TEARDOWN_FUNCTIONS.items() if func["category"] == category}
