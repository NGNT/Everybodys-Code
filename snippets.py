# Code Snippets for insertion inside functions
# These are smaller code pieces that go inside existing functions

CODE_SNIPPETS = {
    # Variables and Objects
    "Find Body by Name": {
        "category": "Objects",
        "code": 'local body = FindBody("body_name")',
        "description": "Find a specific body/object by its name. Replace 'body_name' with the actual name.",
        "variables": ["body"]
    },
    "Find All Bodies": {
        "category": "Objects", 
        "code": "local bodies = FindBodies(\"\")",
        "description": "Find all bodies in the scene. Leave empty quotes to find all, or add a tag.",
        "variables": ["bodies"]
    },
    "Get Body Position": {
        "category": "Objects",
        "code": "local pos = GetBodyTransform(body).pos",
        "description": "Get the position of a body. Requires a body variable.",
        "variables": ["pos"],
        "requires": ["body"]
    },
    "Find Shape by Name": {
        "category": "Objects",
        "code": 'local shape = FindShape("shape_name")',
        "description": "Find a specific shape by its name.",
        "variables": ["shape"]
    },
    "Find All Shapes with Tag": {
        "category": "Objects",
        "code": 'local shapes = FindShapes("tag_name")',
        "description": "Find all shapes with a specific tag.",
        "variables": ["shapes"]
    },
    "Get Shape Body": {
        "category": "Objects",
        "code": "local body = GetShapeBody(shape)",
        "description": "Get the body that contains this shape.",
        "variables": ["body"],
        "requires": ["shape"]
    },
    "Check if Handle Valid": {
        "category": "Objects",
        "code": "if handle ~= 0 and IsHandleValid(handle) then\n    -- Use the handle safely\nend",
        "description": "Always check if handles are valid before using them.",
        "requires": ["handle"]
    },

    # Multiplayer
    "Get All Players": {
        "category": "Multiplayer",
        "code": "local players = GetAllPlayers()",
        "description": "Get a list of all players in the game.",
        "variables": ["players"]
    },
    "Check Input for Player": {
        "category": "Multiplayer",
        "code": 'if InputPressed("interact", player) then\n    -- Player pressed interact\nend',
        "description": "Check if a specific player pressed a key. Use in server.tick().",
        "requires": ["player"]
    },
    "Loop Through All Players": {
        "category": "Multiplayer",
        "code": "local players = GetAllPlayers()\nfor i = 1, #players do\n    local player = players[i]\n    -- Do something with each player\nend",
        "description": "Loop through all players in multiplayer.",
        "variables": ["players", "player"]
    },
    "Get Player Camera": {
        "category": "Multiplayer",
        "code": "local camera = GetPlayerCameraTransform(player)",
        "description": "Get a specific player's camera transform (server-safe).",
        "variables": ["camera"],
        "requires": ["player"]
    },
    "Get Player Interact Shape": {
        "category": "Multiplayer",
        "code": "local interactShape = GetPlayerInteractShape(player)",
        "description": "Get the shape a player is looking at for interaction.",
        "variables": ["interactShape"],
        "requires": ["player"]
    },
    "Sync to Shared": {
        "category": "Multiplayer",
        "code": "shared.myVariable = myValue",
        "description": "Sync server data to clients using shared table.",
        "requires": ["myValue"]
    },
    "Read from Shared": {
        "category": "Multiplayer",
        "code": "local value = shared.myVariable or defaultValue",
        "description": "Read synchronized data from server with safe default.",
        "variables": ["value"]
    },

    # Input
    "Check Key Pressed": {
        "category": "Input",
        "code": 'if InputPressed("key") then\n    -- Do something\nend',
        "description": "Check if a key was just pressed this frame. Replace 'key' with actual key name."
    },
    "Check Key Held": {
        "category": "Input", 
        "code": 'if InputDown("key") then\n    -- Do something while held\nend',
        "description": "Check if a key is being held down. Replace 'key' with actual key name."
    },
    "Check Multiple Keys": {
        "category": "Input",
        "code": 'if InputPressed("interact") or InputPressed("use") then\n    -- Either key pressed\nend',
        "description": "Check for multiple different keys."
    },
    "Get Mouse Position": {
        "category": "Input",
        "code": "local mouseX, mouseY = InputValue(\"mousedx\"), InputValue(\"mousedy\")",
        "description": "Get mouse movement delta.",
        "variables": ["mouseX", "mouseY"]
    },

    # Physics
    "Apply Force to Body": {
        "category": "Physics",
        "code": "SetBodyVelocity(body, Vec(0, 0, 10))",
        "description": "Apply velocity to a body. Change the Vec(x,y,z) values for direction and speed.",
        "requires": ["body"]
    },
    "Explode at Position": {
        "category": "Physics",
        "code": "Explosion(Vec(0, 0, 0), 2.0)",
        "description": "Create an explosion at a position. First Vec is position, second number is size."
    },
    "Explode at Body": {
        "category": "Physics",
        "code": "local pos = GetBodyTransform(body).pos\nExplosion(pos, 2.0)",
        "description": "Create an explosion at a body's position.",
        "variables": ["pos"],
        "requires": ["body"]
    },
    "Spawn Fire": {
        "category": "Physics",
        "code": "SpawnFire(Vec(0, 0, 0))",
        "description": "Spawn fire at a specific position."
    },
    "Apply Impulse": {
        "category": "Physics",
        "code": "local impulse = Vec(0, 10, 0)\nSetBodyVelocity(body, VecAdd(GetBodyVelocity(body), impulse))",
        "description": "Add an impulse to existing body velocity.",
        "variables": ["impulse"],
        "requires": ["body"]
    },
    "Check if Body Broken": {
        "category": "Physics",
        "code": "if IsBodyBroken(body) then\n    -- Body is damaged\nend",
        "description": "Check if a body has been damaged/broken.",
        "requires": ["body"]
    },
    "Make Body Static": {
        "category": "Physics",
        "code": "SetBodyDynamic(body, false)",
        "description": "Make a body static (non-moving).",
        "requires": ["body"]
    },
    "Make Body Dynamic": {
        "category": "Physics",
        "code": "SetBodyDynamic(body, true)",
        "description": "Make a body dynamic (can move).",
        "requires": ["body"]
    },

    # Lighting
    "Find Light": {
        "category": "Lighting",
        "code": 'local light = FindLight("light_name")',
        "description": "Find a light by its name.",
        "variables": ["light"]
    },
    "Find All Lights": {
        "category": "Lighting",
        "code": 'local lights = FindLights("tag")',
        "description": "Find all lights with a specific tag.",
        "variables": ["lights"]
    },
    "Turn Light On": {
        "category": "Lighting",
        "code": "SetLightEnabled(light, true)",
        "description": "Turn on a light.",
        "requires": ["light"]
    },
    "Turn Light Off": {
        "category": "Lighting",
        "code": "SetLightEnabled(light, false)",
        "description": "Turn off a light.",
        "requires": ["light"]
    },
    "Change Light Color": {
        "category": "Lighting",
        "code": "SetLightColor(light, 1, 0, 0)  -- Red light",
        "description": "Change light color. Values are R, G, B from 0 to 1.",
        "requires": ["light"]
    },
    "Flash Light": {
        "category": "Lighting",
        "code": "local flash = math.sin(GetTime() * 10) > 0\nSetLightEnabled(light, flash)",
        "description": "Make a light flash on and off.",
        "variables": ["flash"],
        "requires": ["light"]
    },

    # Sound
    "Load Sound": {
        "category": "Sound",
        "code": 'local sound = LoadSound("MOD/sounds/sound.ogg")',
        "description": "Load a sound file. Put sound files in MOD/sounds/ folder.",
        "variables": ["sound"]
    },
    "Load Looping Sound": {
        "category": "Sound",
        "code": 'local loopSound = LoadLoop("MOD/sounds/loop.ogg")',
        "description": "Load a looping sound file.",
        "variables": ["loopSound"]
    },
    "Play Sound at Position": {
        "category": "Sound",
        "code": "PlaySound(sound, Vec(0, 0, 0), 1.0)",
        "description": "Play a sound at a specific position with volume 1.0.",
        "requires": ["sound"]
    },
    "Play Sound at Body": {
        "category": "Sound",
        "code": "local pos = GetBodyTransform(body).pos\nPlaySound(sound, pos, 1.0)",
        "description": "Play a sound at a body's position.",
        "variables": ["pos"],
        "requires": ["sound", "body"]
    },
    "Play Loop at Position": {
        "category": "Sound",
        "code": "PlayLoop(loopSound, Vec(0, 0, 0), 1.0)",
        "description": "Play a looping sound at a position.",
        "requires": ["loopSound"]
    },

    # UI Drawing
    "Draw Text": {
        "category": "UI",
        "code": 'UiPush()\n    UiTranslate(50, 50)\n    UiColor(1, 1, 1)\n    UiText("Hello World")\nUiPop()',
        "description": "Draw text on screen. Put in client.draw() function."
    },
    "Draw Text at Center": {
        "category": "UI",
        "code": 'UiPush()\n    UiAlign("center middle")\n    UiTranslate(UiWidth()/2, UiHeight()/2)\n    UiColor(1, 1, 1)\n    UiText("Centered Text")\nUiPop()',
        "description": "Draw text at the center of the screen."
    },
    "Draw Colored Text": {
        "category": "UI",
        "code": 'UiPush()\n    UiTranslate(50, 50)\n    UiColor(1, 0, 0)  -- Red\n    UiText("Red Text")\nUiPop()',
        "description": "Draw colored text. Colors are R, G, B from 0 to 1."
    },
    "Draw Rectangle": {
        "category": "UI",
        "code": 'UiPush()\n    UiTranslate(50, 50)\n    UiColor(0, 0, 1)\n    UiRect(100, 50)  -- Width, Height\nUiPop()',
        "description": "Draw a filled rectangle."
    },
    "Draw Progress Bar": {
        "category": "UI",
        "code": 'local progress = 0.5  -- 50%\nUiPush()\n    UiTranslate(50, 50)\n    UiColor(0.2, 0.2, 0.2)\n    UiRect(200, 20)  -- Background\n    UiColor(0, 1, 0)\n    UiRect(200 * progress, 20)  -- Foreground\nUiPop()',
        "description": "Draw a progress bar showing completion percentage.",
        "variables": ["progress"]
    },
    "Draw with Safe Margins": {
        "category": "UI",
        "code": 'local x0, y0, x1, y1 = UiSafeMargins()\nUiPush()\n    UiTranslate(x0 + 50, y0 + 50)\n    UiText("Safe Text")\nUiPop()',
        "description": "Draw UI that works on all screen sizes.",
        "variables": ["x0", "y0", "x1", "y1"]
    },

    # Math and Utility
    "Random Number": {
        "category": "Math",
        "code": "local randomNum = math.random(1, 10)",
        "description": "Generate random number between 1 and 10. Change the range as needed.",
        "variables": ["randomNum"]
    },
    "Random Float": {
        "category": "Math",
        "code": "local randomFloat = math.random()",
        "description": "Generate random float between 0 and 1.",
        "variables": ["randomFloat"]
    },
    "Create Vector": {
        "category": "Math", 
        "code": "local vector = Vec(0, 0, 0)",
        "description": "Create a 3D vector with x, y, z coordinates.",
        "variables": ["vector"]
    },
    "Add Vectors": {
        "category": "Math",
        "code": "local result = VecAdd(vec1, vec2)",
        "description": "Add two vectors together.",
        "variables": ["result"],
        "requires": ["vec1", "vec2"]
    },
    "Vector Distance": {
        "category": "Math",
        "code": "local distance = VecDist(pos1, pos2)",
        "description": "Calculate distance between two positions.",
        "variables": ["distance"],
        "requires": ["pos1", "pos2"]
    },
    "Normalize Vector": {
        "category": "Math",
        "code": "local normalized = VecNormalize(vector)",
        "description": "Make a vector have length 1 while keeping direction.",
        "variables": ["normalized"],
        "requires": ["vector"]
    },
    "Scale Vector": {
        "category": "Math",
        "code": "local scaled = VecScale(vector, 2.0)",
        "description": "Multiply vector by a number to make it longer/shorter.",
        "variables": ["scaled"],
        "requires": ["vector"]
    },
    "Lerp Between Values": {
        "category": "Math",
        "code": "local result = Lerp(startValue, endValue, 0.1)",
        "description": "Smoothly blend between two values. 0.1 = 10% per frame.",
        "variables": ["result"],
        "requires": ["startValue", "endValue"]
    },
    "Clamp Value": {
        "category": "Math",
        "code": "local clamped = math.max(minValue, math.min(maxValue, value))",
        "description": "Keep a value between minimum and maximum.",
        "variables": ["clamped"],
        "requires": ["minValue", "maxValue", "value"]
    },

    # Game State
    "Print to Console": {
        "category": "Debug",
        "code": 'DebugPrint("Hello World")',
        "description": "Print text to the game console for debugging."
    },
    "Print Variable": {
        "category": "Debug",
        "code": 'DebugPrint("Variable: " .. tostring(myVariable))',
        "description": "Print a variable's value to console.",
        "requires": ["myVariable"]
    },
    "Get Current Time": {
        "category": "Timing",
        "code": "local currentTime = GetTime()",
        "description": "Get the current game time in seconds.",
        "variables": ["currentTime"]
    },
    "Wait/Delay": {
        "category": "Timing",
        "code": "if GetTime() > startTime + delay then\n    -- Do something after delay\nend",
        "description": "Simple delay mechanism. You need to set startTime = GetTime() earlier.",
        "requires": ["startTime", "delay"]
    },
    "Frame Rate Timer": {
        "category": "Timing",
        "code": "local deltaTime = dt",
        "description": "Get time since last frame (put in tick function).",
        "variables": ["deltaTime"]
    },
    "Set Registry Value": {
        "category": "Data Storage",
        "code": 'SetString("mymod.setting", "value")',
        "description": "Store a string value that persists between sessions."
    },
    "Get Registry Value": {
        "category": "Data Storage",
        "code": 'local value = GetString("mymod.setting", "default")',
        "description": "Get a stored string value with default fallback.",
        "variables": ["value"]
    },
    "Set Number Registry": {
        "category": "Data Storage",
        "code": 'SetFloat("mymod.number", 42.5)',
        "description": "Store a number value that persists."
    },
    "Get Number Registry": {
        "category": "Data Storage",
        "code": 'local number = GetFloat("mymod.number", 0.0)',
        "description": "Get a stored number with default fallback.",
        "variables": ["number"]
    },

    # Triggers and Locations
    "Find Trigger": {
        "category": "Triggers",
        "code": 'local trigger = FindTrigger("trigger_name")',
        "description": "Find a trigger by its name.",
        "variables": ["trigger"]
    },
    "Check Point in Trigger": {
        "category": "Triggers",
        "code": "if IsPointInTrigger(trigger, position) then\n    -- Point is inside trigger\nend",
        "description": "Check if a position is inside a trigger area.",
        "requires": ["trigger", "position"]
    },
    "Find Location": {
        "category": "Locations",
        "code": 'local location = FindLocation("location_name")',
        "description": "Find a location marker by its name.",
        "variables": ["location"]
    },
    "Get Location Transform": {
        "category": "Locations",
        "code": "local transform = GetLocationTransform(location)",
        "description": "Get the position and rotation of a location.",
        "variables": ["transform"],
        "requires": ["location"]
    },
    "Find All Locations": {
        "category": "Locations",
        "code": 'local locations = FindLocations("tag")',
        "description": "Find all locations with a specific tag.",
        "variables": ["locations"]
    },

    # Raycasting
    "Raycast Forward": {
        "category": "Raycast",
        "code": "local camera = GetCameraTransform()\nlocal hit, dist, normal, shape = QueryRaycast(camera.pos, camera.fwd, 50)",
        "description": "Cast a ray forward from camera to find what player is looking at.",
        "variables": ["camera", "hit", "dist", "normal", "shape"]
    },
    "Raycast Custom": {
        "category": "Raycast",
        "code": "local hit, dist, normal, shape = QueryRaycast(startPos, direction, maxDist)",
        "description": "Cast a ray from custom position in custom direction.",
        "variables": ["hit", "dist", "normal", "shape"],
        "requires": ["startPos", "direction", "maxDist"]
    },
    "Check Line of Sight": {
        "category": "Raycast",
        "code": "local canSee = not QueryRaycast(pos1, VecNormalize(VecSub(pos2, pos1)), VecDist(pos1, pos2))",
        "description": "Check if there's a clear line of sight between two positions.",
        "variables": ["canSee"],
        "requires": ["pos1", "pos2"]
    },

    # Conditional Logic Templates
    "If Statement": {
        "category": "Logic",
        "code": "if condition then\n    -- Do something\nelse\n    -- Do something else\nend",
        "description": "Basic if-else statement template. Replace 'condition' with your logic."
    },
    "Multiple Conditions": {
        "category": "Logic",
        "code": "if condition1 and condition2 then\n    -- Both are true\nelseif condition1 or condition2 then\n    -- At least one is true\nelse\n    -- Neither is true\nend",
        "description": "Template for multiple conditions with and/or logic."
    },
    "For Loop (Count)": {
        "category": "Logic",
        "code": "for i = 1, 10 do\n    -- Repeat 10 times\nend",
        "description": "Loop that repeats a specific number of times."
    },
    "For Loop (List)": {
        "category": "Logic", 
        "code": "for i, item in ipairs(list) do\n    -- Process each item\nend",
        "description": "Loop through a list/table of items.",
        "requires": ["list"]
    },
    "While Loop": {
        "category": "Logic",
        "code": "while condition do\n    -- Keep doing this\n    -- Remember to change condition!\nend",
        "description": "Loop while a condition is true. Be careful to avoid infinite loops!"
    },
    "Switch Statement": {
        "category": "Logic",
        "code": "if value == 1 then\n    -- Case 1\nelseif value == 2 then\n    -- Case 2\nelse\n    -- Default case\nend",
        "description": "Multiple choice logic (like a switch statement).",
        "requires": ["value"]
    },

    # Tags and Properties
    "Set Object Tag": {
        "category": "Tags",
        "code": 'SetTag(handle, "tag_name", "value")',
        "description": "Add a tag with value to an object.",
        "requires": ["handle"]
    },
    "Get Object Tag": {
        "category": "Tags",
        "code": 'local value = GetTag(handle, "tag_name", "default")',
        "description": "Get a tag value from an object with default fallback.",
        "variables": ["value"],
        "requires": ["handle"]
    },
    "Remove Object Tag": {
        "category": "Tags",
        "code": 'RemoveTag(handle, "tag_name")',
        "description": "Remove a tag from an object.",
        "requires": ["handle"]
    },
    "Check if Tag Exists": {
        "category": "Tags",
        "code": 'if HasTag(handle, "tag_name") then\n    -- Object has this tag\nend',
        "description": "Check if an object has a specific tag.",
        "requires": ["handle"]
    },
    "List All Tags": {
        "category": "Tags",
        "code": "local tags = ListTags(handle)",
        "description": "Get all tag names from an object.",
        "variables": ["tags"],
        "requires": ["handle"]
    },
}

# Function templates (complete functions)
FUNCTION_TEMPLATES = {
    "Create Variable": {
        "category": "Variables",
        "code": "local myVariable = value",
        "description": "Create a new variable. Replace 'myVariable' with your name and 'value' with the initial value.",
        "is_template": True
    },
    "Simple Function": {
        "category": "Functions",
        "code": "function myFunction(parameter)\n    -- Your code here\n    return result\nend",
        "description": "Create a custom function template.",
        "is_template": True
    }
}

def get_snippet_categories():
    """Get all unique categories from snippets and templates"""
    all_items = {**CODE_SNIPPETS, **FUNCTION_TEMPLATES}
    return sorted(set(item["category"] for item in all_items.values()))

def get_snippets_by_category(category):
    """Get all snippets in a specific category"""
    all_items = {**CODE_SNIPPETS, **FUNCTION_TEMPLATES}
    return {name: item for name, item in all_items.items() if item["category"] == category}

def is_snippet(name):
    """Check if an item is a code snippet (not a full function)"""
    return name in CODE_SNIPPETS

def is_template(name):
    """Check if an item is a function template"""
    return name in FUNCTION_TEMPLATES