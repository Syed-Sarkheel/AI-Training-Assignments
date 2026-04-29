# Prompt Engineering Results

This assignment compares multiple prompting strategies and how they change model behavior.

---

## Zero-Shot Prompting

### Prompt Used

```text
What is REST API?
```

### Model Response

```text
REST (Representational State Transfer) API is a popular architectural style for designing networked applications. It's not actually an acronym, but rather a set of constraints intended to enable the design of simple web services. Here's a brief explanation:

1. **Resource**: In REST APIs, each data that can be accessed, manipulated, or deleted is considered a resource. Resources are identified by URIs (Uniform Resource Identifiers).

2. **Representation**: A resource can have multiple representations, such as XML, JSON, or plain text. The client chooses the representation format it prefers.

3. **Stateless**: Each request from a client to a server must contain all of the information needed to process the request. The server does not store anything about the ongoing conversations with the client between requests.

4. **Client-Server**: This is a fundamental principle of REST where the client and server are separate entities. The client is responsible for formatting the data for sending, while the server takes care of processing the data.

5. **Cacheable**: Some responses from the server can be cached by clients to reduce network traffic and latency in subsequent interactions. This is achieved through appropriate HTTP response headers.

6. **Uniform Interface**: REST APIs use a set of common methods like GET (retrieve), POST (create), PUT (update), PATCH (partial update), DELETE (delete) to interact with resources, which simplifies the design and implementation of the API.

7. **Layered System**: The architecture is composed of multiple layers, each performing a specific function, but clients and servers are unaware of what other layers exist. This enhances scalability and allows for easier maintenance and evolution of the system.

8. **Code on Demand (optional)**: A REST service can return executable code to the client in some cases, such as Java applets or scripts. However, this feature is not commonly used in most modern REST APIs.
```

### Notes

- No examples or context were given.
- Useful for quick general questions.

---

## Few-Shot Prompting

### Prompt Used

```text
Q: What is HTTP?
A: A protocol used for communication on the web.

Q: What is REST API?
```

### Model Response

```text
A: REST (Representational State Transfer) API is an architectural style for designing networked applications. It's based on representing resources (like a file or database object) with a unique URL and using standard HTTP methods like GET, POST, PUT, DELETE to manipulate these resources. Unlike SOAP or XML-RPC, REST APIs use lightweight data formats like JSON or XML for data interchange.
```

### Notes

- Prior examples guide answer style.
- Better consistency than zero-shot.

---

## Role Prompting

### Prompt Used

```text
System: You are a senior backend engineer.
Explain REST API to a beginner developer.
```

### Model Response

```text
As a senior backend engineer, I'd be happy to explain the concept of REST APIs (Representational State Transfer Application Programming Interface) in a simple and understandable way for a beginner developer!

REST APIs are a common standard for building web services that allow different software systems to communicate with each other over the internet. They are based on the Representational State Transfer (REST) architectural style, which is an approach for designing networked applications focused on simplicity, scalability, and statelessness.

Here are some key points about REST APIs:

1. Resources: In a REST API, everything is considered a resource. This could be anything that the application manages, like a user, a post, or an image. Each resource has a unique URL (Uniform Resource Locator) for identification.

2. CRUD Operations: The primary function of a REST API is to perform CRUD operations (Create, Read, Update, and Delete) on these resources. These operations are usually done by using HTTP methods such as GET (Retrieve), POST (Create), PUT (Update), and DELETE (Delete).

3. Statelessness: One of the main principles of REST is statelessness, which means that the server should not store any client context between requests. Each request from a client to the server must contain all the necessary information for the server to successfully process it.

4. Uniform Interface: REST APIs follow a uniform interface, which means that clients and servers communicate with each other using a standard set of methods (HTTP verbs like GET, POST, PUT, DELETE), headers, status codes, and a predefined data format (like JSON or XML).

5. Client-Server Architecture: REST APIs support the client-server architecture, where the client is responsible for user interface, request generation, and parsing responses from the server. The server manages the persistent state of the application's resources and processes requests from clients.

6. Layered System: REST APIs are designed as a layered system, which allows intermediary layers like proxies, firewalls, and caches to improve performance and security without changing the API itself.

By understanding these concepts, you will have a solid foundation for building your own REST APIs and working with them in various applications! Happy coding!
```

### Notes

- Role affects tone and explanation depth.
- Good for expert guidance or teaching.

---

## Structured Output (JSON)

### Prompt Used

```text
Give response only in JSON:

{
  "definition": "",
  "benefits": [],
  "examples": []
}

Topic: REST API
```

### Model Response

```json
{
  "definition": "REST (Representational State Transfer) API is an architectural style for designing networked applications based on the web. A RESTful service adheres to six design constraints, known as REST constraints: client-server architecture, statelessness, cacheability, uniform interface, layered system, and code on demand (however, the last one is optional and not always implemented).",
  "benefits": [
    "Simplicity: REST APIs are easy to understand due to their simplicity and the use of standard HTTP methods.",
    "Reusability: Resources in REST APIs can be reused in multiple ways.",
    " scalability: REST APIs are highly scalable as they allow for efficient load distribution across multiple servers.",
    "Security: REST APIs can be secured using various security protocols like HTTPS, OAuth, and basic authentication.",
    "Interoperability: REST APIs can work with any programming language or operating system because they rely on standard web protocols."
  ],
  "examples": [
    "Retrieving a list of books from a bookstore's database using the GET method",
    "Updating the details of a specific book using the PUT method",
    "Deleting a book from the database using the DELETE method",
    "Creating a new book in the database using the POST method"
  ]
}
```

### Notes

- Easier to parse in applications.
- Useful for APIs, automations, dashboards.

---

## Summary Comparison

| Method | Strength | Best Use |
|-------|----------|----------|
| Zero-shot | Fast and simple | Basic Q&A |
| Few-shot | Pattern following | Repetitive tasks |
| Role Prompting | Better tone/context | Teaching / Expertise |
| JSON Output | Structured data | Production apps |

---

## Final Thoughts

Prompt engineering improves reliability and usefulness of LLM outputs. Small prompt changes can strongly influence quality, format, and relevance.
