import mysql.connector

# Function to connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            database="EduSchema"
        )
        print("Connected to the database")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to add a new course
def add_course(conn, courseName, courseDescription, startDate, endDate):
    try:
        cursor = conn.cursor()
        insert_query = "INSERT INTO Courses (courseName, courseDescription, startDate, endDate) VALUES (%s, %s, %s, %s)"
        data = (courseName, courseDescription, startDate, endDate)
        cursor.execute(insert_query, data)
        conn.commit()
        print("Course added successfully")
    except mysql.connector.Error as err:
        print(f"Error adding course: {err}")

# Function to update a course
def update_course(conn, courseID, courseName, courseDescription, startDate, endDate):
    try:
        cursor = conn.cursor()
        update_query = "UPDATE Courses SET courseName = %s, courseDescription = %s, startDate = %s, endDate = %s WHERE courseID = %s"
        data = (courseName, courseDescription, startDate, endDate, courseID)
        cursor.execute(update_query, data)
        conn.commit()
        print("Course updated successfully")
    except mysql.connector.Error as err:
        print(f"Error updating course: {err}")

# Function to remove a course
def remove_course(conn, courseID):
    try:
        cursor = conn.cursor()
        delete_query = "DELETE FROM Courses WHERE courseID = %s"
        cursor.execute(delete_query, (courseID,))
        conn.commit()
        print("Course deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error deleting course: {err}")

# Function to search for courses by courseName
def search_courses(conn, courseName):
    try:
        cursor = conn.cursor()
        search_query = "SELECT * FROM Courses WHERE courseName LIKE %s"
        cursor.execute(search_query, ('%' + courseName + '%',))
        courses = cursor.fetchall()
        if courses:
            for course in courses:
                print(course)
        else:
            print("No courses found with that name")
    except mysql.connector.Error as err:
        print(f"Error searching courses: {err}")

# Function to fetch all courses and sort by courseName
def fetch_sorted_courses(conn):
    try:
        cursor = conn.cursor()
        fetch_query = "SELECT * FROM Courses ORDER BY courseName"
        cursor.execute(fetch_query)
        courses = cursor.fetchall()
        if courses:
            for course in courses:
                print(course)
        else:
            print("No courses found")
    except mysql.connector.Error as err:
        print(f"Error fetching courses: {err}")

# Main function to demonstrate usage
def main():
    conn = connect_to_database()
    if not conn:
        return
    
    # Add a new course
    add_course(conn, "Mathematics 102", "Introduction to Mathematics", "2024-09-01", "2024-12-31")

    # Update a course
    update_course(conn, 1, "Mathematics 101", "Basic Mathematics", "2024-09-01", "2024-12-31")

    # Remove a course
    remove_course(conn, 1)

    # Search for courses
    search_courses(conn, "Mathematics")

    # Fetch and sort courses
    fetch_sorted_courses(conn)

    conn.close()

if __name__ == "__main__":
    main()