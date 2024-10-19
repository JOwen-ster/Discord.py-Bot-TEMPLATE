# @app_commands.command(name='canvas-assignments')
# async def canvasassgn(self, interaction: discord.Interaction, classid: int):
#     load_dotenv()
#     canvas = Canvas('https://csufullerton.instructure.com', getenv('CANVAS_TOKEN'))
#     course = canvas.get_course(classid)
#     assgnmts = ''
#     for a in course.get_assignments():
#         assgnmts += (str(a) + '\n')
#     await interaction.response.send_message(embed=BotMessageEmbed(description=assgnmts), ephemeral=True)