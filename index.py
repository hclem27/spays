#Import des modules (Discord notamment)
import os
import discord
import json  
from typing import Text
from discord import member
from discord.ext import commands
from discord.ext.commands.core import check, has_role



bot = commands.Bot(command_prefix = "!", description = "Bot de RYPERK")
client = discord.Client()

@bot.event
async def on_ready():
    print("Ready !")

#Fonction qui est utilisée lorsque l'on envoi !aide dans le tchat et envoie les messages ci dessous
@bot.command()
async def Aide(ctx):
    await ctx.send ("Voici la liste des commandes disponible")
    await ctx.send("!Del {Insérer la valeur} -> Supprimer le nombre de message indiquer")
    await ctx.send("!Sort -> Donne des informations sur les sorts souhaités ")
    await ctx.send("!Classe -> Permet de voir les différentes classes de Dofus et ses variantes")
    await ctx.send("!Contact -> Rassemble l'intégralité de mes réseaux ")
    await ctx.send("!Draft -> Lance une draft de sort (pick & ban)")
    print(ctx.author)

#Fonction qui est utilisée lorsque l'on envoi !Sort dans le tchat, elle permet de récupérer les informations d'un sort (PA, Variante, Effet...)
@bot.command()
async def Sort(ctx):
    await ctx.send("Indiquer la classe")
    classeValeur = await bot.wait_for("message", timeout = 60)
    classe = classeValeur.content
    await ctx.send("Indiquer le sort")
    sortValeur = await bot.wait_for("message", timeout = 60)
    sort = sortValeur.content
    fichier_json = open('spell.json.', 'r', encoding="utf-8")
    with fichier_json as fichier:
        data = json.load(fichier)      # load décode un fichier json
        for datum in data['{}'.format(classe)]:

                    Name = datum['name']
                    CoutPAName = datum['CoutPAName']
                    DetailName = datum['DetailName']
                    Variant = datum['variant']
                    CoutPAVariant = datum['CoutPAVariant']
                    DetailVariant = datum['DetailVariant']

                    SortInName = "{}".format(sort) in Name
                    SortInVariant = "{}".format(sort) in Variant
                   
                    if SortInName == True:
                        await ctx.send("Le sort **{}** coûte {}, {} Sa variante **{}** coûte {}, {}".format(Name, CoutPAName, DetailName, Variant, CoutPAVariant, DetailVariant))
                    elif SortInVariant == True:
                        await ctx.send("Le sort **{}** coûte {}, {} Sa variante **{}** coûte {}, {}".format(Variant, CoutPAVariant, DetailVariant, Name, CoutPAName, DetailName))
                        
                       
#Fonction qui est utilisée lorsque l'on envoi !del(nbr) et supprime le nombre de message voulu
@bot.command(name="Del")
@commands.has_role("Administrateur")
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages +1).flatten()
    for each_message in messages:
        await each_message.delete()

#Fonction qui est utilisée lorsque l'on envoie !Draft et lance une draft de sort entre deux joueurs
@bot.command()
async def Draft(ctx):
    await ctx.send("Le joueur qui a lancé la Draft est **A** 🔴, l'autre joueur est **B** 🔵. Chaque lettre est précisée avant chaque phrase.")
    
    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    def checkEmoji1(reaction, user):
        return SortPickB.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    def checkEmoji2(reaction, user):
        return SortBanB.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")     

    def checkEmoji3(reaction, user):
        return SortPickD.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    def checkEmoji4(reaction, user):
        return SortBanDD.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")        


    listpicka = []
    await ctx.send("🔴 Marquer le premier sort que vous voulez __pick__ 🔴")        
    sorta = await bot.wait_for("message", timeout = 60)
    message = await ctx.send(f"Le sort **{sorta.content}** a été pick par **A** Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji)
    if reaction.emoji == "✅":
        listpicka.append(sorta.content)
    else:
        listpicka.append(sorta.content)
        del listpicka[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        sortaa = await bot.wait_for("message", timeout = 60)
        listpicka.append(sortaa.content)
   
    
    listpickb = []
    await ctx.send("🔵 Marquer le premier sort que vous voulez __pick__ 🔵")
    SortPickB = await bot.wait_for("message", timeout = 60)
    message = await ctx.send(f"Le sort **{SortPickB.content}** a été pick par **B** Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji1)
    if reaction.emoji == "✅":
        listpickb.append(SortPickB.content)
    else:
        listpickb.append(SortPickB.content)
        del listpickb[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        SortPickBB = await bot.wait_for("message", timeout = 60)
        listpickb.append(SortPickBB.content)
     
    listbana = []
    await ctx.send("🔴 Marquer le premier sort que vous voulez __ban__ 🔴")
    sortpicka = await bot.wait_for("message", timeout=60)
    message = await ctx.send(f"Le sort **{sortpicka.content}** a été ban par **A**. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji)
    if reaction.emoji == "✅":
        listbana.append(sortpicka.content)
    else:
        listbana.append(sortpicka.content)
        del listbana[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        sortpickaa = await bot.wait_for("message", timeout = 60)
        listbana.append(sortpickaa.content)
        
    listbanb = []
    await ctx.send("🔵 Marquer le premier sort que vous voulez __ban__ 🔵")
    SortBanB = await bot.wait_for("message", timeout=60)
    message = await ctx.send(f"Le sort **{SortBanB.content}** a été ban par **B**. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji2)
    if reaction.emoji == "✅":
        listbanb.append(SortBanB.content)
    else:
        listbanb.append(SortBanB.content)
        del listbanb[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        SortBanBB = await bot.wait_for("message", timeout = 60)
        listbanb.append(SortBanBB.content)
        
    await ctx.send("🔴 Marquer le sort que vous voulez __pick__ 🔴")
    sortc = await bot.wait_for("message", timeout = 60)
    message = await ctx.send(f"Le sort **{sortc.content}** a été pick par **A** Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji)
    if reaction.emoji == "✅":
        listpicka.append(sortc.content)
    else:
        listpicka.append(sortc.content)
        del listpicka[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        sortpickbb = await bot.wait_for("message", timeout = 60)
        listpicka.append(sortpickbb.content)
        
    await ctx.send("🔵 Marquer le sort que vous voulez __pick__ 🔵")
    SortPickD = await bot.wait_for("message", timeout = 60)
    message = await ctx.send(f"Le sort {SortPickD.content} a été pick par **B** Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji3)
    if reaction.emoji == "✅":
        listpickb.append(SortPickD.content)
    else:
        listpickb.append(SortPickD.content)
        del listpickb[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        SortPickDD = await bot.wait_for("message", timeout = 60)
        listpickb.append(SortPickDD.content)
    
    await ctx.send("🔵 Marquer le deuxième sort que vous voulez __ban__ 🔵")
    SortBanDD = await bot.wait_for("message", timeout=60)
    message = await ctx.send(f"Le sort **{SortBanDD.content}** a été ban par **B**. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji4)
    if reaction.emoji == "✅":
        listbanb.append(SortBanDD.content)
    else:
        listbanb.append(SortBanDD.content)
        del listbanb[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        SortBanDDD = await bot.wait_for("message", timeout = 60)
        listbanb.append(SortBanDDD.content)
        
    await ctx.send("🔴 Marquer le deuxième sort que vous voulez __ban__ 🔴")
    sortpicka1 = await bot.wait_for("message", timeout=60)
    message = await ctx.send(f"Le sort **{sortpicka1.content}** a été ban par **A**. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reaction, user = await bot.wait_for("reaction_add", timeout = 60, check = checkEmoji)
    if reaction.emoji == "✅":
        listbana.append(sortpicka1.content)
    else:
        listbana.append(sortpicka1.content)
        del listbana[-1]
        await ctx.send("Marquer le sort que vous souhaitez modifier")
        sortpicka11 = await bot.wait_for("message", timeout = 60)
        listbana.append(sortpicka11.content)
        
    await ctx.send(" 🔴 **A** Vos sorts bannis par le joueur **B** sont **{}**. Vous avez décidé de jouer avec les sorts suivants : **{}** 🔴".format(listbanb, listpicka))
    await ctx.send(" 🔵 **B** Vos sorts bannis par le joueur **A** sont **{}**. Vous avez décidé de jouer avec les sorts suivants : **{}** 🔵".format(listbana, listpickb))
    await ctx.send("La draft est terminée. Bon match!🔴🔵")


@bot.command()
async def Contact(ctx):
    await ctx.send("TWITTER - RYPERKK")
    await ctx.send("TWITTER - SPAYSD")
    await ctx.send("YOUTUBE - RYPERK")
    await ctx.send("DISCORD - RYPERK#8744")
    await ctx.send("MAIL - RYPERK.CONTACT@GMAIL.COM")

@bot.command()
async def Classe(ctx):
    await ctx.send("Si vous souhaitez avoir des informations sur une classe précise veuillez marquer le nom de la classe. Exemple : Iop")
    classe = await bot.wait_for("message", timeout=60)
    message = await ctx.send(f"Vous souhaitez des informations sur **{classe.content}**")
    if classe.content == "Iop":
        await ctx.send("Pour connaître les sorts et les variantes du Iop : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/8-iop")
    elif classe.content == "Feca":
        await ctx.send("Pour connaître les sorts et les variantes du Feca : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/1-feca")
    elif classe.content == "Ecaflip":
        await ctx.send("Pour connaître les sorts et les variantes de l'Ecaflip : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/6-ecaflip")
    elif classe.content == "Eniripsa":
        await ctx.send("Pour connaître les sorts et les variantes de l'Eniripsa : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/7-eniripsa")
    elif classe.content == "Cra":
        await ctx.send("Pour connaître les sorts et les variantes du Crâ : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/9-cra")
    elif classe.content == "Sacrieur":
        await ctx.send("Pour connaître les sorts et les variantes du Sacrieur : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/11-sacrieur")
    elif classe.content == "Sadida":
        await ctx.send("Pour connaître les sorts et les variantes du Sadida : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/10-sadida")
    elif classe.content == "Osamodas":
        await ctx.send("Pour connaître les sorts et les variantes de l'Osamodas : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/2-osamodas")
    elif classe.content == "Enutrof":
        await ctx.send("Pour connaître les sorts et les variantes de l'Enutrof : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/3-enutrof")
    elif classe.content == "Sram":
        await ctx.send("Pour connaître les sorts et les variantes du Sram : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/4-sram")
    elif classe.content == "Xelor":
        await ctx.send("Pour connaître les sorts et les variantes du Xélor : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/5-xelor")
    elif classe.content == "Pandawa":
        await ctx.send("Pour connaître les sorts et les variantes du Pandawa : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/12-pandawa")
    elif classe.content == "Roublard":
        await ctx.send("Pour connaître les sorts et les variantes du Roublard : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/13-roublard")
    elif classe.content == "Zobal":
        await ctx.send("Pour connaître les sorts et les variantes du Zobal : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/14-zobal")
    elif classe.content == "Steamer":
        await ctx.send("Pour connaître les sorts et les variantes du Steamer : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/15-steamer")
    elif classe.content == "Eliotrope":
            await ctx.send("Pour connaître les sorts et les variantes de l'Eliotrope : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/16-eliotrope")
    elif classe.content == "Huppermage":
            await ctx.send("Pour connaître les sorts et les variantes de l'Huppermage : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/17-huppermage")
    elif classe.content == "Ouginak":
            await ctx.send("Pour connaître les sorts et les variantes de l'Ouginak : https://www.dofus.com/fr/mmorpg/encyclopedie/classes/18-ouginak")
    else:
        await ctx.send("Aucune classe de selectionnée")

    
bot.run("ODUzOTY0NjEwMTkzMzI2MDgw.YMdChA.PhyyMRrEZtjLQuyJVrMJC80kpyE")



"""
#pick a
pick b
ban a
ban b
pick a
pick b
--
ban b
ban a
pick b
pick a
✅❌
"""

