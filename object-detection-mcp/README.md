### Пример использования

#### Сборка образа

В терминале, в папке с Dockerfile этого MCP сервера запустите следующую команду:

```
docker build -t mcp-object-detector .
```

Имя образа можете заменить на любое) главное дальше используйте то же имя.

#### Подключение MCP сервера к Claude Desktop

Добавьте в соответствующую секцию `"mcpServers"` вашего файла `claude_desctop_config.json`.

```
"object-detector": {
    "command": "docker",
    "args": [
        "run",
        "-i",
        "--rm",
        "--mount",
        "type=bind,src=/Users/ilnarshafigullin/Desktop/ilnar/Anthropic/demo,dst=/projects,ro",
        "mcp-object-detector:latest"
    ]
}
```

`src` - это папка на вашем компьютере, замените на актуальную для вас.
