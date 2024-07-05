"""
Cogs are useful for organizing ur code
You'll be needing them
"""

import os, discord

class StartUp:

 async def startup(bot):
    await bot.wait_until_ready()

 async def loadcogs(self): 
  for folder in ["./cogs"]:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                if file.endswith(".py"):
                    try:
                        await self.load_extension(f"{folder[2:].replace('/', '.')}.{file[:-3]}")
                        print(f"Loaded plugin {file[:-3].lower()} from {folder}")
                    except Exception as e:
                        print(f"Failed to load {file[:-3]} from {folder}: {e}")