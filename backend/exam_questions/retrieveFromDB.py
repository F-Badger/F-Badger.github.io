def getQuestions(topics):
    import mysql.connector
    from writeToDB import getTopicIDs

    #connect to the database
    database= mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="examquestions"
    )

    cursor = database.cursor() #create MySQLCursor object to allow interaction with database

    #use function from writeToDB.py to get list of topic IDs
    topicIDs = getTopicIDs(topics, cursor)

    #format query to retrieve the wanted data from the database
    query = f"\
    SELECT tbl_examquestions.question_id, extended_response, question_img, ms_img\n\
    FROM tbl_examquestions\n\
    JOIN tbl_questiontopicjunction ON tbl_examquestions.question_id = tbl_questiontopicjunction.question_id\n\
    WHERE tbl_questiontopicjunction.topic_id in ({','.join(map(str,topicIDs))})"

    #execute the query
    cursor.execute(query)

    #get the query results
    results = cursor.fetchall()

    #output results for testing
    for result in results:
        print (f"Question ID: {result[0]}\nExtended Response: {result[1]}\nQuestion Image: {result[2]}\nMark Scheme Image; {result[3]}")
        
    #close cursor and database connection
    cursor.close()
    database.close()

getQuestions(["1.2.1","1.1.1"])