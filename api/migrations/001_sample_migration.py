steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE project (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            img_url VARCHAR(300) NOT NULL,
            description TEXT NOT NULL,
            github_url VARCHAR(300) NOT NULL,
            live_url VARCHAR(300)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE project;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE contact (
            id SERIAL PRIMARY KEY,
            name VARCHAR(200) NOT NULL,
            phone VARCHAR(15),
            email VARCHAR(200) NOT NULL,
            message TEXT NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE contact;
        """
    ],
]
