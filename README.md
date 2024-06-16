# Chat Room 🗨️

Chat Room is a real-time messaging application that allows users to send messages instantly to a group. It supports features such as text-based communication, user authentication, and real-time updates.

## Features

1. **Admin Control**: Admins have the ability to create topics for rooms and perform CRUD operations on rooms.
2. **User Authentication**: Users must be authenticated to join any room.
3. **Joining Rooms**: Authenticated users can join any room.
4. **Messaging**: Authenticated users can send and read all messages in the room.

## Installation

To get started with Chat Room, follow these steps:

1. Install Django:
```pip install django```

2. Install Channels for real-time updates:
```python -m pip install daphne```

3. Install Docker (if not already installed) for containerization:
[Docker Installation Guide](https://docs.docker.com/get-docker/)

```docker run -p 6379:6379 -d redis:5```
```python3 -m pip install channels_redis```

4. Install MySQL client for database interaction:
```pip install mysqlclient```



## Usage

To run the Chat Room application, follow these steps:

1. Clone the repository:
```git clone https://github.com/MeMadDev/code_room.git```


2. Navigate to the project directory:
```cd code_room```

3. Set up the Django environment and migrate the database:
```python manage.py migrate```

4. Start the development server:
```python manage.py runserver```

5. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).