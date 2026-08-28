# Meeting with Bruno and Gabriel (Andrei Mikriukov)

**Fecha:** 2026-06-05T13:59:51.436+00:00  
**Duración:** ~61 min  
**Participantes:** Aleksandr Belikov <aleksandr.belikov@constructor.tech>, Bruno Ruyu <bruno@teramot.com>, Lucio Rojas <lucio@teramot.com>, Andrei Mikriukov <andrei.mikriukov@constructor.org>, Anastasiia Ivankova <anastasiia.ivankova@constructor.tech>  
**Externos:** aleksandr.belikov@constructor.tech, andrei.mikriukov@constructor.org, anastasiia.ivankova@constructor.tech  
**Apollo ID:** 6a22e4ccee3c0300144182ba

---

**Lucio Rojas**: It.

**Bruno Ruyu**: Sa. Endurance.

**Lucio Rojas**: Hello.

**Bruno Ruyu**: Hi.

**Lucio Rojas**: Hi.

**Bruno Ruyu**: Hello. I think Andrei Mikrikov is about joining in several minutes. So I. I think it's better maybe to wait if. If it's okay for you. Sure, yeah, we can wait. No problem.

**Andrei Mikriukov**: Hi, everyone.

**Bruno Ruyu**: Hi.

**Lucio Rojas**: Hi.

**Andrei Mikriukov**: I'm very sorry for the delay. German trains never arrive on schedule and it's freaking rainy today in Bremen. I wish I could talk to you from the outside, but it's so rainy. I'm listening. And I'll be in front of my laptop in like three minutes. But we could start if everybody else is here.

**Bruno Ruyu**: Sorry, sorry, I was muted. Sorry for that. I was saying yes now I was saying hi. So I don't know if you can see our camera. I'm here, Bruno, with Gabriel in this meeting. In the meeting room. Sorry. And also Lucio on another one. He has been helping you guys with connecting the info, as. I understand. So we thought of also making him join the co.

**Andrei Mikriukov**: I could also introduce our team here. We have Anastasia and Alexander. So basically I'm doing research at Constructor. As you might know, Constructor is a huge company, huge ecosystem of companies, and our team is responsible for different types of research for the entire ecosystem. And Alexander here and there are our analysts. Nastasia is covering the technical part. He's mostly working with our databases, dashboards, data analysis and so on. Alexander is covering. He knows the content very well since we are mostly focusing on education and science. Alexander knows a lot about different policies, about different data, about different countries. So he's covering content parts. He's covering technical part. And yeah, I invite them to this meeting because they provided data for this test and also they've already tested some in the interface, so I'd like to keep them in the loop as well.

**Bruno Ruyu**: Perfect, thank you.

**Andrei Mikriukov**: Shall we proceed? Will you show us some demo at the beginning or we start with question that we already had? I mean, we've explored the platform very briefly on our own, without guidance. So maybe if you could show us how we were supposed to use the platform, it could be. Maybe better.

**Bruno Ruyu**: Yeah. Okay. Well, so Lucio, if you have the. The workspace and the project, I mean, you are okay if we use that to show you the ones that you.

**Andrei Mikriukov**: Sure, sure, sure.

**Lucio Rojas**: So yeah, sure, I can show screen.

**Bruno Ruyu**: Yeah, yeah, exactly, please. Sure. If you can do that, we can take it from there and show the usage,

**Andrei Mikriukov**: but

**Bruno Ruyu**: you use the tool, the msb and name some queries, I think you could get to that.

**Andrei Mikriukov**: Sorry, I didn't fully understand the question. But yes, we've tried first to upload our data and then to

**Bruno Ruyu**: kind of

**Andrei Mikriukov**: a browse through it using the interface inside. And I think. And see, I also tried to connect The MCP from ChatGPT and from Cloud. And you can correct me if I'm wrong.

**Lucio Rojas**: Yeah, that's right.

**Andrei Mikriukov**: Yeah, I already have some.

**Bruno Ruyu**: Okay. Okay.

**Andrei Mikriukov**: Initial knowledge about how it works, but brief.

**Bruno Ruyu**: Okay. So then we can discuss a little bit of what you encounter. But as a first part we can. Lucio will show you how it's used and so you can see. So just for the beginning, he's already inside the workspace. Perhaps you can move one step before and show that you have many workspaces.

**Lucio Rojas**: Yes.

**Bruno Ruyu**: So you can. Workspaces. This was just one. So there he can go and find the one that. The one that we are talking about. So once inside the workspace you have projects. So nothing weird, but there he can create a project. I mean, it's just like any tool. So you don't need to do it well, you know. So once. So in the. In the project that you got the info here is the. So in the left you have a bar. Basically the most important parts are there. First is the. You have it in Spanish.

**Lucio Rojas**: Yes, I'm going to change that quickly. Yeah, no problem with that. For English now. Okay, enjoy.

**Bruno Ruyu**: Yeah.

**Lucio Rojas**: Okay.

**Bruno Ruyu**: So there is the data sources and then what is called Data Studio. So data sources. Here is where Lucio help you guys connect. Go back please. Lucio connect the different. I don't know exactly what type of information you share. Okay. If you wanted to connect different type of source, you would go to connect sources. I mean you could upload files, which is probably what Lucio did. But then you can. This is when you just upload the files. If you have tabular like CSV access and in connect sources you go and you. You select the direct connection to a database or a data warehouse or a type of solution. And basically you can. Yeah, you just. There and it's a typical connector show data. No science here. And that establish a permanent connection in which you can define the logic and the frequency and the timing of that connection. Like a typical connectivity database. Nothing weird. And the it where you define the refresh frequency, the schedule and basically that's. So after you. You connect what. What happened in the background was. Sorry. When you connect, you have the flexibility to go and select. If you connect to a database that has, I don't know, 400 tables. Perhaps you are thinking of a project that only needs 50. So you select only those 50 tables. And if for some reason you don't want to upload a certain column because it could be something that you don't want to use or whatever reason you have the granularity to select to the columns that are going to be uploaded. And once you start that uploading process, what will happen in Terramon it would make. It basically will copy the information on what we call the bronze layer of the data lakehouse. The bronze layer is something that we know we don't show anywhere because we don't believe that makes much sense because it's just the dump the same information you had on your previous source. But once the bronze layer is connected, the first part of the ancient start working and they create the silver layer where information is already enriched with metadata. And also the fixing the findings and the fixing problems have already worked to create for each table a SQL query that transforms in the cases that it needs to be transformed. And that is something that you can already see here in the Data Studio section. You have in that selector the different tables that were uploaded and that were transformed so you can first explore the different tables. And this is a place where you can run your own query if you want to just explore it in a way that makes sense for you. And then if you keep it in the same table, move the table, you can go to see creation details that basically shows some information about that and the transformation that it did. In this case it did nothing because it was already filed. I don't know if you checked. Perhaps there was something you can try to see in some tables. I know if you did that to see if there was some transformation. Lucio try to show a couple of them to see if there was a transformation made in any of them. I mean, sure. I. I don't know because of. I didn't work with this, So probably did not. Perhaps you can ask. It would be better, right? Yeah. So instead of doing this manually, we can just. The MCB can check the SQLs. Yeah, so well, what. Yeah. Okay. Then we see how it was connected. Yeah, continue, continue. Then we can show them how the permission is made. And see if any silver table was.

**Lucio Rojas**: I'm going to change the language quickly.

**Andrei Mikriukov**: I think we're using code so much so that interface is actually understandable. It will probably reason in English. Yeah, because.

**Bruno Ruyu**: There. Yeah, take all the table. All the single tables and see if any higher transformation. Probably this is a curated data set. It probably might not need many confirmations. But of course, you know. Yeah, those are official data provided with API. So probably yeah, it was clean Enough already. Okay, so what. But you know, in the real life case there will be some transformations and formatting fixes, some casting deletion of some duplicates. Well, you have the select listing there, some removal of nulls. So the typical thing that you do. But let's take a look, perhaps it will find it. But wait, wait, wait, wait. Wait for him. Don't get distracted. We don't know what. And see how it works after that. So this is the silver layer. So after that the important thing is make the MCP connector So Claude or ChatGPT or whatever AI can see and start using Terra. So don't download to the old templates yet, go to the mc. There are basically the instructions on how to do it. I don't know if. You were able to do the connector and it worked or you had a problem there.

**Andrei Mikriukov**: Yeah, it worked.

**Lucio Rojas**: But it expires from the site of

**Andrei Mikriukov**: GPT in like 30 minutes.

**Bruno Ruyu**: It wasn't stable all the time in chatgpt expired. And which type of connection did you do the. Can you scroll down a little bit? Lucio again? You know there. There are several ways of make the connection. You did this one right?

**Lucio Rojas**: Yeah, before.

**Bruno Ruyu**: Okay, it's weird, but we will take a look because we didn't have anybody reporting that, but we'll take a look. And it was in the Anastasia. Did you use your personal account or. It's a team account. Okay, we'll take a look into that and see what might have happened. But basically the. You know the process of making a financial is just getting the URL from the yes and adding the id. Of course you can either use the rare tokens if you want, but I think this is the easy way. If you use the browser version and after that after making the connection then you would. I mean what we do is we use Claude to. To basically start working as we were working here there. So there it found some logic select this thing.

**Lucio Rojas**: All these tables only have a select distance that's not some formation. And this one inconvenient logic found. We can ask for that or we can just use the tool to ask what is in the tables.

**Bruno Ruyu**: So wait, so it shows here that only one table had a transformation. So with this cast from something to double that is all you did. So that's the only information. And now after that, here's the moment in which you start creating whatever analysis or just asking for. For whatever objective you need to accomplish with those tables. So I don't know, I don't know exactly what you have here, but yeah, we should try asking for. You can ask Claude what. What type of analysis we can do with all this information. Try to see what they offers and. And then we run it.

**Andrei Mikriukov**: But all the reasoning will go from clothes right here.

**Bruno Ruyu**: Claude will use the terramod tools to explore what information is available and then. And suggest what. Yeah, it would reason and say we can do this, this. It will be done by Claude and then we will say okay, do this analysis and it will create tables in the go layer.

**Andrei Mikriukov**: What tools are available inside your mcp?

**Bruno Ruyu**: Can you show it Lucio?

**Andrei Mikriukov**: I think yeah, Cloud can actually show it. Right.

**Bruno Ruyu**: Yeah, it's here.

**Lucio Rojas**: Discover schema download. Notice.

**Andrei Mikriukov**: Okay. So quite a lot.

**Bruno Ruyu**: Yeah.

**Lucio Rojas**: Yes.

**Andrei Mikriukov**: Is it only get or also you can change that.

**Bruno Ruyu**: You can create. You can go down and you have the create.

**Andrei Mikriukov**: Okay, list.

**Lucio Rojas**: You can list process.

**Andrei Mikriukov**: It's also get.

**Lucio Rojas**: Yes, and then we have create tools here. User create ETL source project secret. You can create a gold table,

**Bruno Ruyu**: go down a little bit more. You can even delete and duplicate. Change the access work on the menu.

**Andrei Mikriukov**: Okay. Okay.

**Bruno Ruyu**: So the logic would be we just. We use some type of analysis that Cloth should perform and then we will ask to perform one and it will start sending instructions to Teramo to create these non layered tables. The instructions are sent in natural language and Terramot interprets that with all the information, all the metadata, all the knowledge and creates a SQL query. TerraMot is the one writing the queries.

**Lucio Rojas**: So here you can choose one. Take a look at this possible analysis that the. Otherwise then we can try out one.

**Bruno Ruyu**: I will try to find something that is complex. So we would.

**Andrei Mikriukov**: Yeah, something like that maybe uses like two or three tables.

**Bruno Ruyu**: Yeah, we can even ask is there any of these analysis. I would use three or four tables

**Andrei Mikriukov**: binders and ventricle is called. I don't know. And what is the next one? Sasha, you choose.

**Bruno Ruyu**: I think the last one sounds great. Or is it again is it from one table that the data will be from one day?

**Andrei Mikriukov**: Since the. I think that they are listing sources and it's like.

**Bruno Ruyu**: Yeah, yeah, it's multi.

**Andrei Mikriukov**: Yeah, multi table.

**Bruno Ruyu**: Yeah, use that one. Use the last one. Right?

**Andrei Mikriukov**: Yeah, yeah, let's try this one.

**Bruno Ruyu**: Yeah, yeah.

**Lucio Rojas**: Okay. We're okay with this one with full scrolling.

**Andrei Mikriukov**: Yes.

**Lucio Rojas**: Okay. And now we can see how the two use TerraMot to create the new code table. You can see the query, the request and how they interact between them.

**Andrei Mikriukov**: This it could take a while.

**Bruno Ruyu**: I guess it would take five, a couple of minutes. Not that long.

**Lucio Rojas**: Not that long. Maybe five or to ten minutes is the time. This is interesting. Here is where Claude showed the instructions to Terramot to how to create the new code table. Here is where Claude takes place from the human that needs to write that instructions and you just ask what you want and it happens this incredible sport. I don't know if you have any questions while we wait for the gold computation.

**Andrei Mikriukov**: Maybe you could tell us again the difference between gold and silver tables.

**Bruno Ruyu**: So. Basically silver tables are the input tables that were cleaned. In this case, since the data was already super clean, it only made one transformation. It cast one column to another to double.

**Andrei Mikriukov**: Yeah, okay.

**Bruno Ruyu**: So basically the silver is the cleaned input and it's all that you selected. So if it was an SAP databases or Oracle, whatever, you just import all those tables and the you run all the the cleaning transformations and those are the silvers. The goals are the ones that are built for a purpose purpose for an analysis for. So here we asked for those scorecard. So we created one go table called. So so basically goals are the end products in the value added like that. I mean the value is added all around the process, but the combination of that is the goal table where the information is already joined and transformed to whatever analysis you need to perform. And in this case, since we were asking kind of random stuff, it just created one gold table. But sometimes you need to create for one particular important or not important, but profound analysis. It might need to create 2, 3, 4. It depends on what you ask. Basically we have a. For instance, just an example if you want to create or the user wants to create an app to send emails to increase sales of their retail products. For that, it will create one table to understand which is the elasticity to price for the different users for the different products. Then it will create another table to understand the probability of purchase per user per product. Then it will create another table to. I don't know, to basically understand which are the seasonality of products. And then it will create another one to make estimations of discounts that should be made for each users. And then all of that goes into an app that summarizes how much discount you can provide to a different user for a different product. So for a complex case that that or another. Sorry, another one would be segmentation of customers. So if you ask something sufficiently complex, then you probably create more than one goal table. In this case it was just one because it was quite simple what we asked and this is, sorry, the result.

**Lucio Rojas**: Yes, in cloud cells, the the table is already created slide. This is a new ETL source And here we have the OP table Bruno, that will continue if you want. Okay. And here you can say, you can see the new table that is created that takes four sibling tables. This difference, this is the output and these are the inputs that you give to us. And if you. You can see the description, that is. I don't know if you want to read it. Here is school scorecard for 20, 25. One row per school. That's showing Escoda Matricula data center and Turma tables. Includes school identify and location files, key infrastructure, binary indicators, Internet library accessibility, labs, sports. Yeah, it's just description of the table.

**Bruno Ruyu**: If you. I mean if you. You scroll down, you can see what is the exact query that it wrote. And there is a. The human text explanation of what it did. So a human can see afterwards what is there and understand it without the need of understanding SQL code. And then afterwards you see the real SQL code. So just scroll it. It doesn't matter. I mean. We are seeing something different. Yeah. Okay, So this is what's just joining tables because we asked something quite simple. Right. But we can move into something much more complex if you want. Right? Right. So

**Lucio Rojas**: what. What you already did.

**Bruno Ruyu**: Ah, this is one created by you, right?

**Lucio Rojas**: Yes. Instructions.

**Bruno Ruyu**: Just so there you just. Just copy the table. Basically what you asked before. So I will go to Claude and say we need something more complex. This is not adding value.

**Andrei Mikriukov**: Maybe that we provide is not so insightful. What can we get about education institutions? Right.

**Bruno Ruyu**: What you provide. Exactly. Say what you suggested. It wasn't that insightful. We need to understand in much more deepness. You are saving tokens. I don't see you and so insightful enough.

**Andrei Mikriukov**: I saw research that says that if you will type most of your prompts in Chinese, you would save like 20% of tokens. You need to learn Chinese and you'll just add like. Please reply in English and it will work well. And

**Lucio Rojas**: maybe what can we ask now? I want more complex.

**Bruno Ruyu**: Yeah, I want a more much. A much more complex analysis with. With real insights.

**Lucio Rojas**: Sorry. Okay. Maybe you have a question to the data sets that you want to do to test the tool. I mean the ones who choose the data set for the demo. And you want us to ask for it?

**Bruno Ruyu**: Go ahead.

**Lucio Rojas**: Okay,

**Bruno Ruyu**: while we wait, I would like to share here in the chat or I can send it in an email. There was an article published today by Lantropic that basically they show how hard is to do what Teramount does. That is for my summary of the article. So basically they say how we can use Claude or Analytics, I mean you can read it and basically they end up saying that it's a month length, month length project with it with a very, I mean an anthropic engineering team which speaks by himself the level of expertise that they have and that is something that requires for the way in which they did it, which is different from what we do that it requires permanent maintenance and they basically say we need to keep a human in the loop. So I think it's a good validation for us because it basically states the anthropic engineering team is struggling to do this. Basically I won't say that we have to solve it because that would be probably, I mean I cannot affirm but I can definitely affirm that we are on the right track on the user experience and the non requirement of technical team in our customers for what Thermal does. So I think it's a very nice discussion. I will need to read it again two or more three times to understand it in depth. But probably something that you might be interested to read. Yeah, we don't need to read it now.

**Lucio Rojas**: No problem. As we wait. Now it's making a new map of kind of analysis that you can do to. Oh group. Here.

**Bruno Ruyu**: Wait, so he started doing analysis? No, no, no, he said no, we, we need to build an analysis. Okay, yeah, yeah. Okay.

**Andrei Mikriukov**: The gold tables that he creates.

**Bruno Ruyu**: Yeah, yeah. So ask for that and let's see what it does. But I mean I don't know if you want to continue this but we can create that one to see if it's more context. And start. Just stop this.

**Lucio Rojas**: Okay. Analysis with states Internet. Okay, it's working. And see the legal table here in

**Andrei Mikriukov**: a few minutes While we are waiting.

**Lucio Rojas**: Yes.

**Andrei Mikriukov**: May I ask some questions as I understand most of the database providers such as like Supabase or NAS, Nocodb, Mongodb, Mariadb, Clickhouse, they are also building their MCPs like built in. For example we saw the MCP from Clickhouse. It is quite well. It is quite well developed. Well developed I could say you have like only I don't know four or five different tools there and it's. Well Claude hallucinates a lot using this MCP or sometimes when you have a lot of information. For example here we uploaded only like 10 tables our database we have hundreds of them and sometimes you have similar information in different tables. Like for example you may have a list of universities for the country or a list of universities which are ranked in times higher education ranking and this MCP would take if we'll ask like list us all universities and amount of students budget whatever specific country it might be that our MCP will find only ranking table. And these does universities which are in ranking, which is obviously not true because not all universities are ranked and so on. So it hallucinates. It don't hallucinates, it just does bad job. But in general I believe most of them will still work on their MCPS and they will evolve. So how much different from those internal solutions position Terra mode Amazing.

**Bruno Ruyu**: So the for me the most. I don't know. It's important but the most clear difference is that we offer something that is completely agnostic. And in reality companies information is not just in one in one solution. So SAP can have their agents if you want, but if they need to use that with the CRM that is safe force then it makes you know, is useless. And basically there would be some use cases in which information can come from only just one source, but they are really AT D. So that is something that we were always super clear from. The first line of code is that we are agnostic to the origin of information and information from whatever connector we can. And in the second, and secondly, of course it would depend on which is the approach of this type of tools, the different tools and MCP that different companies would use. But for me it was great to read that this approach of building a real data engineering pipeline that was a solution that we understood from the day we read the transformer paper that this would be the only real solution. Because of course I I worked for 10 years at data analyst, data engineering, data scientist. Then I was chief data officer. And I know that the only way to work with data is making an organized structure. It's impossible. And, and I think in the paper of Anthropic there's a section that is called Data is not software. It's a different piece. It's not the same in data. It can happen what you say in one table you have. And it happened to me many times. I used to work in an oil and gas company. So we sometimes refer to the fields the oil field by the surface facilities. Sometimes we refer to the field based on the subsurface Russian war. Sometimes we use like political divisions between provinces. Sometimes we use based on the ownership of the different companies. So you have a lot of ways where you can you just say okay, oil field Bruno. No, I mean there's not one definition. So the only way is to create different entities. And, and for that you need to. For me the way to do that is structure. That Already and write metadata to inform the user about that. The user used to be humans that would need to go to the data management system or whatever governance and read in human text. Okay, no, you are talking about the. What are you doing? I am calculating the royalties. Okay. So you need to go to the political division to see to which province or state you need to pay the royalties. Okay, use that. And that is basically what telemode does. One of the things it writes, infers and writes that. So the other processes are already informed and that kind of solves what you mentioned. I'm not sure if the guys in those companies will do that or will go with for a easier approach or a different approach that is, I don't know, some of them might even do a rag. I mean I remember having discussions with companies in 2023 saying no, but we will need this, we will do a rag and that's it. And I think that the evidence is now that it won't work. So I'm not sure. What we are sure is that this approach, building a data lakehouse or whatever data structure particularly this is a data lakehouse in the medallion architecture is something that solves the problem at a high level. And I know if they will be able to do that if they have the interest of building that. I mean, for what I know no other company from that list or similar to the ones that you mentioned are taking this approach. They are solving it in different ways, writing skills, making some type of other solutions, some of. I mean there's the largest software company in Argentina, it's called Globant, is that unicorn. And we, we already have a partnership with them and they were using a totally different approach. They were trying to create industry.

**Andrei Mikriukov**: Yeah.

**Bruno Ruyu**: Kind of building solutions with industries like verticalized by industry and trying to like make super prompts for different industries. So there's a lot of people trying different approaches and we believe this is the correct one because it's basically replicating the way in which we did by humans, but at a 100x speed. And for that we have a provisional pattern that we submitted the definitive filing last week. So I don't know if that is something that will be an asset, but definitely something that will put us in a discussion if somebody goes for this approach.

**Andrei Mikriukov**: Yeah, that's. That's great.

**Bruno Ruyu**: And basically that is. That is my answer to that. And of course I cannot know exactly what everybody's doing, but for sure, with four tools I'm not. I can't imagine how it would work. I mean definitely.

**Andrei Mikriukov**: Yeah, I Get it? Yeah, thank you. That's comprehensive answer. Clear.

**Bruno Ruyu**: So let's see if the Gold demo.

**Andrei Mikriukov**: It actually created some.

**Bruno Ruyu**: Yeah, and this is the hard part about. And that is a very important insight that we discovered in the last month. When we do demos with companies that we are actively trying to sell, we do our best to do it with real data that they own because then they have like interesting questions to post or analysis to do because they basically struggle to do themselves. And that is a very important moment when they see here something that they were not able to see before and they get there in an hour is like a very important selling point. So have you checked the goal table if the transformation was interesting? Lucio? Yeah, just listen to. Ah, he's frozen.

**Andrei Mikriukov**: Yeah, I think he and his screen are frozen.

**Bruno Ruyu**: Frozen.

**Lucio Rojas**: I can hear you. Yes, I'm screen.

**Bruno Ruyu**: Okay, just one table now is.

**Lucio Rojas**: Is this one?

**Andrei Mikriukov**: Yes, I think so. Yeah.

**Bruno Ruyu**: Well it's not.

**Andrei Mikriukov**: It might be because.

**Lucio Rojas**: Yes, but it's a complex information. Yes. It's only one table, a one table table. But it has a lot of interactions and transformations, SQL transformations. So if you want you can see the query. You have access Android to the use case. I think you can share also with the rest of the team. Keep on pushing in the tool. This is complex for you. We can

**Bruno Ruyu**: copy

**Lucio Rojas**: and here cloud made like a preview of the dashboard sort by the gap. We can ask for computer lab gap and then shows computer gap. Just shows the gaps severity, the difference between plural and urban. Okay. This is cloud doing what

**Bruno Ruyu**: I think there's an interesting one that you can show because it's ours is the. The Gold Unified Users GTM v3, the one that you shared to me. I think that is a complex one because this is basically. Lucio will show you the ones that we use to track our customers usage. And I know that it's complex because it fits like from 12 tables or something like that and it makes a lot of transformations. It's a long instruction. Lucifer. Yes.

**Lucio Rojas**: This is my own use case. My problem here was that we have two systems, we use a server now we're in the app because we improved some things in the back end in the UI and we need to know how many new users we have between the two systems and to unify the different source information. And it was not just a single query to a table of how many users I have. It's a query to many tables that needs to be related between them. We have here two database one from RF, that's the new App Hub one from Server and different CSVs that has another information to enrich the query. So I need to make all these instructions to reach the table that I need to have and make this separate query that is really complex here something particular that's. I'm not a technical guy, I'm from a business and I could do this in my own without help.

**Bruno Ruyu**: Continue scrolling down to see how long it is.

**Lucio Rojas**: Okay, this is a really long query because we have to make many shines between different sources and we reach a table that we think is the source of truth of the users that we had. So then what I did is create a data share and share this call with each one of the my teammates. Yes. So they can consult on their own how many use case users they have. I don't have access to the goal that I share. And he also can ask to the silver tables whether I want I. If I want just to share the gold table I just share the gold table with him and then he can ask to this single source of truth that I made for my. My boss in this case I hope it's. It's a good.

**Bruno Ruyu**: The possibility is that he creates it. We know that it's right because we made the. We checked and now he share with all of us. And it's just one more table that I have at my disposal and I can continue building on top of that. I mean I can use that also as an input for a new go table. So go tables are output but could be input for new calculations if I want to enrich it with something else if I want to summarize it by order or whatever. And the logic is that it's like the single source, not single one of the sources of truth in particular single for the user case. And it was quite a complex stuff to arrive at but with the use of Claude as the one sending the instructions Lucio mentioned he has no SQL query skills so it would be impossible for him if he got it in number of hours.

**Lucio Rojas**: Here we. We upload different data sources. We have a postgres here, some asset string etc inside Here connection from BigQuery are multiple sources that we gather here in the. In the tool and we join them.

**Andrei Mikriukov**: So.

**Bruno Ruyu**: Yeah, so just just to show you like a real use case. I know that.

**Andrei Mikriukov**: Well yeah, I mean that's clear and we probably much better understand how to use it right now. So we will try to play with it a bit more and we'll upload some other our data. More complicated data.

**Bruno Ruyu**: Yeah, yeah that would definitely be interesting. I would check the chat GPT connection problem. If something is there and please keep us posted. Any questions, we are at your disposal. I mean happy to have expert users that you tested the tool. That is something always very valuable.

**Andrei Mikriukov**: Thank you very much for your time.

**Lucio Rojas**: I think we have another question, little one.

**Andrei Mikriukov**: Yeah, sure.

**Lucio Rojas**: About like file like huge motor gbytes because there is limit for uploading files and we have really huge ones.

**Andrei Mikriukov**: So is it like demo version limit or.

**Bruno Ruyu**: Yeah, so that was some. That is why we want users like you because we already improved the tool based on that. Perhaps Lucio, you. I mean I know what you did, but probably you know more the details.

**Lucio Rojas**: Yes, it's. It's just the same that we said on the mail. It was a file with too many columns and files. It was like 12 million route I think. So when we tried first to run didn't work through and then we split that let's say in many parts and it's fits well now we. We work on that and it's already fixes. Fix it so it's not a problem anymore. Okay.

**Bruno Ruyu**: Yeah, yeah, yeah. It was that we were. We didn't have anybody.

**Lucio Rojas**: Right.

**Bruno Ruyu**: But the large data sets that we have tend to be from databases. So the connectors they are already solved that complexity for files we didn't import everything at once. And that is the logic that partitionates the ingestion of the files. But that is.

**Andrei Mikriukov**: That's clear. Yeah. I can show you some other. I don't know bug that I've seen.

**Bruno Ruyu**: Yeah, sure.

**Andrei Mikriukov**: So I hope you can see my screen.

**Lucio Rojas**: Yes, yes.

**Andrei Mikriukov**: Yeah. So I just asked a simple question. It provided me some reply. It's in the chat that is inside the platform.

**Bruno Ruyu**: Yeah.

**Lucio Rojas**: Yes.

**Andrei Mikriukov**: Then I asked another question and tried to, I don't know, create something and it created a table which is not in English. Even though my questions and all the communication was previously in English.

**Bruno Ruyu**: Yeah, same for me.

**Andrei Mikriukov**: And actually it can, you know, switch from Spanish to English like volunteer layers.

**Bruno Ruyu**: There is even Portuguese what I can read.

**Andrei Mikriukov**: You know Spanish or Portuguese. But yes, because data from Brazil.

**Bruno Ruyu**: The information is about the schools in Brazil, but you can ask to English. So yeah, we will. Okay, I will report that. Thanks.

**Andrei Mikriukov**: But I believe that this won't be problem when you use it with the MSP because the cloth will definitely translate everything to English. But we'll assume that you speak English. And even if data in table is in local languages, it will still translate everything.

**Bruno Ruyu**: Just for you to know that that model in the. In the page is not the best one I think it is haiku or something like that.

**Andrei Mikriukov**: Yeah. Yeah, I understand.

**Bruno Ruyu**: Maybe it's not the best performance, but I understand.

**Andrei Mikriukov**: Yeah, of course. I understand how it works on such inside chats, but yeah, just I don't know for you to know.

**Bruno Ruyu**: Okay. Okay.

**Lucio Rojas**: So. Well, you had my email. We are open to feedback, to questions. Happy to, to be there for you. Okay.

**Andrei Mikriukov**: So thank you very much. Yeah, it was a pleasure. Have a great weekend.

**Bruno Ruyu**: Thank you, guys.

**Andrei Mikriukov**: Thank you.

**Bruno Ruyu**: Thank you very.
