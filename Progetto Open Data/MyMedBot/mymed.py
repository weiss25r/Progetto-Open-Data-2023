#Sviluppato da Andrea Spinelli

import logging
from rdflib import *
from telegram import * 
from telegram.ext import * 
from geopy.distance import great_circle

async def start(update,context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Ci sono")

async def find(update,context):
    structure = update.message.text
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Invia la tua posizione...")
    
    if(structure == "/farmacie"):
        return FARMACIE
    elif(structure == "/parafarmacie"):
        return PARAFARMACIE
    elif(structure == "/privati"):
        return PRIVATE
    elif(structure == "/pubblici"):
        return PUBBLICHE
    
    return ConversationHandler.END

async def list_pa(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_pa"):
        return await farmacie_pa(update,context)
    elif(structure == "/parafarmacie_pa"):
        return await parafarmacie_pa(update,context)
    elif(structure == "/privati_pa"):
        return await private_pa(update,context)
    elif(structure == "/pubblici_pa"):
        return await pubbliche_pa(update,context)
    
    return ConversationHandler.END

async def list_ag(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_ag"):
        return await farmacie_ag(update,context)
    elif(structure == "/parafarmacie_ag"):
        return await parafarmacie_ag(update,context)
    elif(structure == "/privati_ag"):
        return await private_ag(update,context)
    elif(structure == "/pubblici_ag"):
        return await pubbliche_ag(update,context)
    
    return ConversationHandler.END

async def list_cl(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_cl"):
        return await farmacie_cl(update,context)
    elif(structure == "/parafarmacie_cl"):
        return await parafarmacie_cl(update,context)
    elif(structure == "/privati_cl"):
        return await private_cl(update,context)
    elif(structure == "/pubblici_cl"):
        return await pubbliche_cl(update,context)
    
    return ConversationHandler.END

async def list_ct(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_ct"):
        return await farmacie_ct(update,context)
    elif(structure == "/parafarmacie_ct"):
        return await parafarmacie_ct(update,context)
    elif(structure == "/privati_ct"):
        return await private_ct(update,context)
    elif(structure == "/pubblici_ct"):
        return await pubbliche_ct(update,context)
    
    return ConversationHandler.END

async def list_en(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_en"):
        return await farmacie_en(update,context)
    elif(structure == "/parafarmacie_en"):
        return await parafarmacie_en(update,context)
    elif(structure == "/privati_en"):
        return await private_en(update,context)
    elif(structure == "/pubblici_en"):
        return await pubbliche_en(update,context)
    
    return ConversationHandler.END

async def list_me(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_me"):
        return await farmacie_me(update,context)
    elif(structure == "/parafarmacie_me"):
        return await parafarmacie_me(update,context)
    elif(structure == "/privati_me"):
        return await private_me(update,context)
    elif(structure == "/pubblici_me"):
        return await pubbliche_me(update,context)
    
    return ConversationHandler.END

async def list_rg(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_rg"):
        return await farmacie_rg(update,context)
    elif(structure == "/parafarmacie_rg"):
        return await parafarmacie_rg(update,context)
    elif(structure == "/privati_rg"):
        return await private_rg(update,context)
    elif(structure == "/pubblici_rg"):
        return await pubbliche_rg(update,context)
    
    return ConversationHandler.END

async def list_sr(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_sr"):
        return await farmacie_sr(update,context)
    elif(structure == "/parafarmacie_sr"):
        return await parafarmacie_sr(update,context)
    elif(structure == "/privati_sr"):
        return await private_sr(update,context)
    elif(structure == "/pubblici_sr"):
        return await pubbliche_sr(update,context)
    
    return ConversationHandler.END

async def list_tp(update,context):
    structure = update.message.text
    
    if(structure == "/farmacie_tp"):
        return await farmacie_tp(update,context)
    elif(structure == "/parafarmacie_tp"):
        return await parafarmacie_tp(update,context)
    elif(structure == "/privati_tp"):
        return await private_tp(update,context)
    elif(structure == "/pubblici_tp"):
        return await pubbliche_tp(update,context)
    
    return ConversationHandler.END

async def farmacie(update,context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)

    await findIn(update, context, user_location.latitude, user_location.longitude,"Farmacia")
    
    return ConversationHandler.END

async def farmacie_pa(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Palermo') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Palermo:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_ag(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Agrigento') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Agrigento:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_cl(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Caltanissetta') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Caltanissetta:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_ct(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Catania') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Catania:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_en(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Enna') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Enna:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_me(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Messina') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Messina:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_rg(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Ragusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Ragusa:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_sr(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Siracusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Siracusa:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def farmacie_tp(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res a sso:Farmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Trapani') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Farmacie a Trapani:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n")     

    return ConversationHandler.END

async def parafarmacie(update,context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)

    await findIn(update, context, user_location.latitude, user_location.longitude,"Parafarmacia")
    
    return ConversationHandler.END

async def parafarmacie_pa(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Palermo') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Palermo:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_ag(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Agrigento') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Agrigento:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_cl(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Caltanissetta') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Caltanissetta:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_ct(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Catania') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Catania:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_en(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Enna') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Enna:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_me(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Messina') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Messina:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_rg(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Ragusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Ragusa:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_sr(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Siracusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Siracusa:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def parafarmacie_tp(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:Parafarmacia .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Trapani') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]

    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Parafarmacie a Trapani:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private(update,context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)

    await findIn(update, context, user_location.latitude, user_location.longitude,"StrutturaPrivata")
    
    return ConversationHandler.END

async def private_pa(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Palermo') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Palermo:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_ag(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Agrigento') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Agrigento:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_cl(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Caltanissetta') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Caltanissetta:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_ct(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Catania') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Catania:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_en(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Enna') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Enna:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_me(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Messina') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Messina:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_rg(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Ragusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Ragusa:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_sr(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Siracusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Siracusa:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def private_tp(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPrivata .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Trapani') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Private a Trapani:\n")
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche(update,context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)

    await findIn(update, context, user_location.latitude, user_location.longitude,"StrutturaPubblica")
    
    return ConversationHandler.END

async def pubbliche_pa(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Palermo') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Palermo:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_ag(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Agrigento') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Agrigento:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_cl(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Caltanissetta') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Caltanissetta:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_ct(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Catania') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Catania:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_en(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Enna') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Enna:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_me(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Messina') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Messina:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_rg(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Ragusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Ragusa:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_sr(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Siracusa') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Siracusa:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def pubbliche_tp(update,context):

    res = g.query("""
                SELECT ?name
                WHERE {
                    ?res rdf:type sso:StrutturaPubblica .
                    ?res sso:hasName ?name .
                    ?res sso:hasSite ?site .
                    ?site sso:isIn ?comune .
                    ?comune sso:hasName ?province .
                    FILTER REGEX(?province,'Trapani') .
                }
                ORDER BY ASC(?name)
                """)

    names = [str(i[0]) for i in res]
    
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Elenco Strutture Sanitarie Pubbliche a Trapani:\n") 
    for item in names:
        await context.bot.send_message(chat_id = update.effective_chat.id, text = "- " + item + "\n") 

    return ConversationHandler.END

async def findIn(update,context,user_lat,user_lon,tipology):

    res = g.query("""
                SELECT ?name ?lat ?lon
                WHERE {
                    ?res rdf:type sso:""" + tipology + """.
                    ?res sso:hasName ?name.
                    ?res sso:hasSite ?site.
                    ?site sso:hasLatitude ?lat.
                    ?site sso:hasLongitude ?lon.
                }
                """)

    names = [str(i[0]) for i in res]
    lats = [float(i[1]) for i in res]
    lons = [float(i[2]) for i in res]

    for a,b,c in zip(names,lats,lons):
        name = a
        my_lat = b
        my_lon = c
            
        dist = great_circle([user_lat,user_lon], [my_lat,my_lon]).meters
        if  dist < 2000:
            await context.bot.send_message(chat_id = update.effective_chat.id, text = name + ":")
            await context.bot.send_location(chat_id = update.effective_chat.id, latitude = my_lat, longitude = my_lon)

    return ConversationHandler.END

def cancel(bot, update):
    bot.sendMessage(update.message.chat_id, "Bye!")
    return ConversationHandler.END

### --- MAIN --- ###

base_uri = "http://www.sanitasicilia.it/resource/"
g = Graph()

sso = Namespace("http://www.sanitasicilia.it/ontology/")
g.bind("sso", sso)

ssr = Namespace("http://www.sanitasicilia.it/resource/")
g.bind("ssr", ssr)

g.parse('../datasets/rdf/sanitasicilia.ttl')

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger("main")

FARMACIE, PARAFARMACIE, PRIVATE, PUBBLICHE = range(4)

if __name__ == '__main__':

    persistence = PicklePersistence(filepath="conversationbot")
    application = ApplicationBuilder().token('6095372312:AAF2UBsvp91TGTDEsloM2on3Fw-W7gipix0').persistence(persistence).build()

    conv_handler = ConversationHandler(
            entry_points=[
                    CommandHandler('start', start),
                    CommandHandler('farmacie', find),
                    CommandHandler('parafarmacie', find),
                    CommandHandler('privati', find),
                    CommandHandler('pubblici', find),
                    CommandHandler('farmacie_pa', list_pa),
                    CommandHandler('parafarmacie_pa', list_pa),
                    CommandHandler('privati_pa', list_pa),
                    CommandHandler('pubblici_pa', list_pa),
                    CommandHandler('farmacie_ag', list_ag),
                    CommandHandler('parafarmacie_ag', list_ag),
                    CommandHandler('privati_ag', list_ag),
                    CommandHandler('pubblici_ag', list_ag),
                    CommandHandler('farmacie_cl', list_cl),
                    CommandHandler('parafarmacie_cl', list_cl),
                    CommandHandler('privati_cl', list_cl),
                    CommandHandler('pubblici_cl', list_cl),
                    CommandHandler('farmacie_ct', list_ct),
                    CommandHandler('parafarmacie_ct', list_ct),
                    CommandHandler('privati_ct', list_ct),
                    CommandHandler('pubblici_ct', list_ct),
                    CommandHandler('farmacie_en', list_en),
                    CommandHandler('parafarmacie_en', list_en),
                    CommandHandler('privati_en', list_en),
                    CommandHandler('pubblici_en', list_en),
                    CommandHandler('farmacie_me', list_me),
                    CommandHandler('parafarmacie_me', list_me),
                    CommandHandler('privati_me', list_me),
                    CommandHandler('pubblici_me', list_me),
                    CommandHandler('farmacie_rg', list_rg),
                    CommandHandler('parafarmacie_rg', list_rg),
                    CommandHandler('privati_rg', list_rg),
                    CommandHandler('pubblici_rg', list_rg),
                    CommandHandler('farmacie_sr', list_sr),
                    CommandHandler('parafarmacie_sr', list_sr),
                    CommandHandler('privati_sr', list_sr),
                    CommandHandler('pubblici_sr', list_sr),
                    CommandHandler('farmacie_tp', list_tp),
                    CommandHandler('parafarmacie_tp', list_tp),
                    CommandHandler('privati_tp', list_tp),
                    CommandHandler('pubblici_tp', list_tp)
                ],
            states={
                FARMACIE: [MessageHandler(filters.LOCATION, farmacie)],
                PARAFARMACIE: [MessageHandler(filters.LOCATION, parafarmacie)],
                PRIVATE: [MessageHandler(filters.LOCATION, private)],
                PUBBLICHE: [MessageHandler(filters.LOCATION, pubbliche)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
            name="mymed",
            persistent=True,
        )

    application.add_handler(conv_handler)
    
    application.run_polling()