### Описание

В репозитории 3 папки с MCP серверами, которые я демонстрирую на видео. 

Если вы хотите воспользоваться этими инструментами, вам необходим Docker на вашем компьютере, и необходимо собрать образы для каждого из инструментов (инструкция есть в каждой папке, включая терминальную команду. Не забывайте вызывать ее из папки с конкретным MCP сервером).

Ниже мой claude_desktop_config.json для референса:

```
{
    "mcpServers": {
        "filesystem": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "--mount",
                "type=bind,src=/Users/ilnarshafigullin/Desktop/ilnar/Anthropic/demo,dst=/projects",
                "mcp/filesystem",
                "/projects"
            ]
        },
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
        },
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
        },
        "clarificator": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "ilnar/clarification-mcp"
            ]
        }
    }
}
```