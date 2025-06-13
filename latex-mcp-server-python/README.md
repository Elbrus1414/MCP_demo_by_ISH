### Пример использования

#### Сборка образа

В терминале, в папке с Dockerfile этого MCP сервера запустите следующую команду:

```
docker build -t ilnar/latex-mcp .
```

Имя образа можете заменить на любое) главное дальше используйте то же имя.

#### Подключение MCP сервера к Claude Desktop

Добавьте в соответствующую секцию `"mcpServers"` вашего файла `claude_desctop_config.json`.

```
"latex-beamer": {
    "command": "docker",
    "args": [
        "run",
        "-i",
        "--rm",
        "--mount",
        "type=bind,src=/Users/ilnarshafigullin/Desktop/ilnar/Anthropic/demo,dst=/projects",
        "ilnar/latex-mcp:latest"
    ]
}
```

`src` - это папка на вашем компьютере, замените на актуальную для вас.
