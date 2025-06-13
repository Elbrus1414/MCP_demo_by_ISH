### Пример использования

#### Сборка образа

В терминале, в папке с Dockerfile этого MCP сервера запустите следующую команду:

```
docker build -t ilnar/clarification-mcp .
```

Имя образа можете заменить на любое) главное дальше используйте то же имя.

#### Подключение MCP сервера к Claude Desktop

Добавьте в соответствующую секцию `"mcpServers"` вашего файла `claude_desctop_config.json`.

```
"clarificator": {
    "command": "docker",
    "args": [
        "run",
        "-i",
        "--rm",
        "ilnar/clarification-mcp"
    ]
}
```