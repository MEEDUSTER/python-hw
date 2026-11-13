from django.shortcuts import render


def index(request):
    context = {
        "nickname": "MEEDUSTER",
        "full_name": "Сергій Олійник",
        "photo_url": "https://avatars.githubusercontent.com/u/196541947?v=4",
        "city": "Вінниця, Україна",
        "email": "leyplayveb@gmail.com",
        "phone": "+380977503857",
        "phone_display": "+380 97 750 38 57",
        "roles": [
            "CEO",
            "Розробник",
            "Головний тестер RML",
            "Адміністратор RML",
        ],
        "github_url": "https://github.com/MEEDUSTER",
        "github_label": "github.com/MEEDUSTER",
        "about": (
            "Мене звати Сергій Олійник. Я CEO і розробник, живу у Вінниці. "
            "З 2026 року навчаюсь у ВНТУ на спеціальності «Комп'ютерні науки». "
            "Займаюсь веб- і мобільною розробкою, роблю проєкти на React, "
            "React Native, Python і Django. У проєкті RML я головний тестер "
            "і адміністратор."
        ),
        "qualities": [
            "Уважність до деталей",
            "Відповідальність",
            "Самостійність",
            "Організованість",
        ],
        "goal": "Далі розвивати свої проєкти, вчитися і працювати як розробник.",
        "education": {
            "institution": "Вінницький національний технічний університет (ВНТУ)",
            "specialty": "Комп'ютерні науки",
            "years": "з 2026",
        },
        "programming_languages": [
            "JavaScript / TypeScript",
            "Python",
            "HTML / CSS",
            "PHP",
        ],
        "software": [
            "Git",
            "GitHub",
            "React",
            "React Native",
            "Django",
            "Flask",
            "Expo",
        ],
        "foreign_languages": [
            {"name": "Українська", "level": "рідна"},
        ],
        "projects": [
            {
                "title": "RML",
                "subtitle": "Головний тестер і адміністратор",
                "description": (
                    "Беру участь у проєкті RML — консольній обгортці над "
                    "бібліотекою rmlib для встановлення та запуску Minecraft. "
                    "У команді я головний тестер і адміністратор: перевіряю "
                    "роботу лаунчера, збираю помилки й допомагаю вести проєкт."
                ),
                "technologies": ["RML", "rmlib", "тестування"],
                "result": "Основна роль у команді RML — тестування та адміністрування.",
                "link": "https://github.com/musdev13/rmlib",
            },
            {
                "title": "react_homeworks",
                "subtitle": "Збірка домашніх робіт з React",
                "description": (
                    "Репозиторій з навчальними роботами на React: "
                    "панель завдань, стрічка новин, лічильники, "
                    "хрестики-нулики та інші завдання курсу."
                ),
                "technologies": ["React", "TypeScript", "Vite"],
                "result": "Усі роботи зібрані в одному репозиторії на GitHub.",
                "link": "https://github.com/MEEDUSTER/react_homeworks",
            },
            {
                "title": "reactnative-hws",
                "subtitle": "Домашні роботи з React Native",
                "description": (
                    "Навчальні мобільні проєкти на React Native і Expo, "
                    "зокрема travel-wishlist із картою подорожей."
                ),
                "technologies": ["React Native", "TypeScript", "Expo"],
                "result": "Репозиторій із роботами курсу на GitHub.",
                "link": "https://github.com/MEEDUSTER/reactnative-hws",
            },
            {
                "title": "autopoint",
                "subtitle": "Лабораторна робота №3",
                "description": (
                    "Статичний сайт AutoPoint, викладений на GitHub Pages."
                ),
                "technologies": ["PHP", "HTML", "CSS"],
                "result": "Лабораторна опублікована як окремий репозиторій.",
                "link": "https://github.com/MEEDUSTER/autopoint",
            },
        ],
    }
    return render(request, "main/index.html", context)
