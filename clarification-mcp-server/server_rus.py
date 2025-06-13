#!/usr/bin/env python3
"""
simple_clarification_mcp.py — простой рабочий MCP-сервер для уточнений.

Минимальная версия без сложных типов данных.
"""
from __future__ import annotations

import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("simple-clarification-mcp")


app = FastMCP(
    name="simple-clarification-mcp",
    version="1.0.0", 
    description="Простой сервер для запроса уточнений",
)


@app.tool()
def request_clarification(context: str) -> str:
    """
    Запрашивает дополнительную информацию у пользователя, когда исходный запрос слишком общий,
    оставляет несколько возможных трактовок или не содержит критически важных деталей.

    Вызывайте функцию, если:
      • есть риск выполнить действие, которое может оказаться бесполезным, неточным или нежелательным;
      • формулировка запроса допускает разные направления работы («исследования про контактные линзы»,
        «построй график продаж», «сгенерируй дизайн» и т. д.);
      • не хватает параметров (формат, объём, метрики, сроки, целевая аудитория);
      • требуется согласовать уровень детализации результата, методику или критерии оценки.

    Args:
        context (str): Краткое объяснение, что именно необходимо уточнить 
                       (одно-два предложения, без излишних деталей).

    Returns:
        str: Дружелюбный вопрос на русском языке, который можно сразу 
             отправить пользователю для прояснения запроса.
    """
    
    prompt = f"Мне нужно уточнение по поводу: {context}. Подскажите, пожалуйста, как следует поступить?"
    
    log.info(f"Generated clarification for: {context}")
    return prompt


@app.tool()
def ask_project_details(unclear_requirement: str) -> str:
    """Запросить детали для проектной задачи.
    
    Используется когда пользователь просит создать систему/приложение,
    но требования неоднозначны.
    
    Args:
        unclear_requirement: Что именно неясно в требованиях
        
    Returns:
        Вопрос пользователю для уточнения
    """
    
    prompt = f"Чтобы создать подходящее решение, уточните: {unclear_requirement}"
    
    log.info(f"Asked for project details about: {unclear_requirement}")
    return prompt


if __name__ == "__main__":
    app.run()
