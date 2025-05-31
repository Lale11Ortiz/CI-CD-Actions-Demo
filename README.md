# 🚀 Proyecto CI/CD - GitHub Actions Demo

## 📂 Estructura del repositorio
CI-CD-Actions-Demo/
- .github/
    - workflows/
        - python-ci.yml      🟢 Flujo de trabajo CI/CD
- Automation/
    - __init__.py
    - test_ci_cd_ok.py      ✅ Test de verificación CI/CD
- .gitignore
- README.md                 📘 Este archivo

---

Este repositorio forma parte de la **Temporada 3** – Arco 2 del viaje de aprendizaje como **QA Automation Engineer**, con foco en la integración y despliegue continuo (**CI/CD**) mediante **GitHub Actions**.

---

## 🛠️ Tecnologías utilizadas

- `Python 3.11`
- `unittest`
- `GitHub Actions`
- `flake8` (análisis de calidad de código)
- `CI/CD` (Integración Continua / Entrega Continua)

---

## ⚙️ Automatización y Workflow

La acción principal está definida en el archivo: .github/workflows/python-ci.yml

Este flujo de trabajo (`workflow`) se activa **automáticamente** cuando se hace `push` a `main`. Ejecuta los siguientes pasos:

1. 🔄 Verifica el entorno.
2. 📦 Instala dependencias.
3. 🧪 Ejecuta tests unitarios con `unittest`.
4. 📏 Verifica la calidad del código con `flake8`.

---

## ✅ Archivo de test principal

`Automation/test_ci_cd_ok.py`

Este archivo contiene un test de validación para verificar si GitHub Actions está correctamente configurado y puede ejecutar pruebas con unittest en entornos automatizados.

---

## ✍️🏽 Notas de desarrollo
- Se realizaron varios intentos fallidos de integración como parte del proceso de aprendizaje.

- Todos los errores fueron resueltos aplicando buenas prácticas de debugging, calidad de código (PEP8) y formateo.

- Este proyecto representa el primer contacto exitoso con CI/CD en la nube mediante herramientas modernas.