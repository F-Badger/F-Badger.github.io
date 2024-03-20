def writeToDatabase(year, level, paper, extendedResponse, questionNum, questionImg, msImg, topics):
    import mysql.connector

    #connect to the database
    database= mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="examquestions"
    )

    cursor = database.cursor() #create MySQLCursor object to allow interaction with database

    questionID = f"{year}_{level}_{paper}_{questionNum}" #create questionID (primary key) by combining the year, level, paper and question number

    topicIDs = getTopicIDs(topics, cursor) #get list of topic IDs

    #create SQL query to add data to tbl_examquestions
    #not needed to specify which fields to insert values into as all fields are being entered
    newEntryQuestionTbl = f"INSERT INTO tbl_examquestions VALUES ('{questionID}','{year}','{level}','{paper}',{extendedResponse},'{questionNum}','{questionImg}','{msImg}');"

    #create SQL query to add data to tbl_questiontopicjunction
    newEntryJunctionTbl = "INSERT INTO tbl_questiontopicjunction VALUES "
    
    #add a new line to the above query for each record necesary for the number of topics
    for index, topicID in enumerate(topicIDs):
        newRecord = f"('{questionID}',{topicID})"
        
        #add a comma to the end apart from for the last item
        if index < len(topicIDs)-1: 
            newRecord += ","

        newEntryJunctionTbl += newRecord

    #execute the queries to add records to the relevant tables
    cursor.execute(newEntryQuestionTbl) 
    cursor.execute(newEntryJunctionTbl)

    database.commit() #commit the transaction

    #close cursor and database connection
    cursor.close()
    database.close()

def getTopicIDs(topics, cursor):
    topicIDs = [] #initialise list of topicIDs

    #query to retrieve topicIDs using topic names
    query = "SELECT topic_id \
                FROM tbl_topics WHERE \
                topic_name = %s"
    
    #execute query for each topic to get the corresponding topicIDs, adding them to the list of topicsIDs
    for topic in topics:
        cursor.execute(query, (topic,)) #(topic,) converts topic into a tuple of one element, which is necessary for syntax
        topicID = cursor.fetchone()[0]
        topicIDs.append(topicID)

    return topicIDs