
# Web Fundamentals Lecture Notes

## Brief History of the Web

In 1989, a computer scientist at CERN named Tim Berners-Lee proposed the idea of information being accessed and shared seamlessly across a widespread network of computers. This proposal laid the foundation for the World Wide Web (WWW), revolutionizing how we access and share information.

## Client-Server Model

Websites are hosted on servers, and we use clients (such as a web browser) to send a request via a URL to the server to access the website. The server responds with the website data. As you navigate the website, you will notice the URL in your browser changes when you change pages or access different resources. Each time it changes, the handshake of request and response between client and server happens behind the scenes.

Browsers are the portals through which we access the World Wide Web. They allow us to navigate the internet and interpret web content, converting code into the text, images, and videos we see on our screens.

## Web Architectures

### Monolithic Architecture

The entire application is encapsulated into a single unified codebase, and all the application functionalities are intertwined. This architecture is great for quick deployment but can have trouble scaling functionalities. Examples of applications that were or are monolithic include:

- **Airbnb** (transitioning to other architectures)
- **SoundCloud**
- **Facebook** (was monolithic in its early days)
- Most e-commerce applications today

### Service-Oriented Architecture (SOA)

Applications are broken down into distinct services and components, each covering a broad range of responsibilities. This architecture is common in applications such as:

- **Customer Relationship Management (CRM) systems**
- **Product Information Management (PIM) systems**

### Microservice Architecture

This architecture is composed of numerous small, highly specialized modules, each performing a unique function and communicating via a lightweight mechanism. It is used for high scalability, as each module can be developed and deployed independently. Facebook is an example of a company that has transitioned to this architecture.

## Briefing on Site Communications

### REST (Representational State Transfer)

REST is the standard communication protocol, which allows for CRUD (Create, Read, Update, Delete) communication. It is widely used for its simplicity and scalability in web services.

### GraphQL

GraphQL allows for specialized requests, ensuring efficient and precise data exchanges. It provides more flexibility compared to REST by allowing clients to request exactly what they need and nothing more.

### gRPC (Google Remote Procedure Calls)

Developed by Google, gRPC is a high-speed, low-latency communication protocol that compresses the messages between client and server, making it suitable for real-time applications.

### WebSocket

WebSockets open a continuous two-way communication channel, unlike the traditional request-response model. They are used in applications requiring real-time communication, such as live streaming and live video games.

## Virtual Environments

Creating a virtual toolbox with all the tools required for your application to run is a key step in managing the dependencies of your application without overloading your system.

### Creating a Virtual Environment

#### Windows:
```sh
python -m venv venv
```

#### MacOS:
```sh
python3 -m venv venv
```

### Activating the Virtual Environment (Opening Your Toolbox)

#### Windows:
```sh
venv\Scripts\activate
```

#### MacOS:
```sh
source venv/bin/activate
```

### Saving/Installing Project Requirements

*MAKE SURE YOUR VIRTUAL ENVIRONMENT IS ACTIVATED*

#### Storing project requirements
```bash
pip freeze > requirements.txt
```

#### Installing from requirements.txt
```bash
pip install -r requirements.txt
```



### Installing Packages (Adding to Your Toolbox)

Use `pip` to install packages in your virtual environment.

*MAKE SURE YOUR VIRTUAL ENVIRONMENT IS ACTIVATED*

#### Example:
```sh
pip install <package name>
```

#### Specific Packages:
- To make HTTP requests:
```sh
pip install requests
```
- To parse HTML data:
```sh
pip install beautifulsoup4
```

