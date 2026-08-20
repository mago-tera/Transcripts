# Skill: `upload-transcript`

Skill de Claude Code para el equipo de Teramot. Convierte la transcript de una
reunión en un markdown estandarizado (4 secciones), lo sube a este repo
(`mago-tera/Transcripts`) y actualiza el deal correspondiente en Attio.

## Qué hace

1. Sintetiza la transcript en 4 secciones: **Caso de uso**, **Roles y áreas
   afectadas**, **Testimonios y valor**, **Señales de compra**.
2. Sube el `.md` a este repo vía la API de GitHub.
3. En Attio (objeto `deals`): busca el deal (lo crea si no existe), agrega una
   nota con el resumen + link, actualiza `next_step` y `last_contact`, y mueve el
   `stage` solo cuando la señal es clara.

## Requisitos (una vez por persona)

- **Claude Code** instalado.
- Acceso de **escritura** al repo `mago-tera/Transcripts` (o estar logueado con
  `gh auth login` en una cuenta con permiso).
- Conector **Attio** autorizado (workspace Teramot) — en claude.ai › Connectors,
  o `/mcp` en Claude Code.
- Conector **Apollo** autorizado (opcional, solo si vas a tirar transcripts
  directo desde Apollo en vez de pegarlas).

## Instalación

Copiá la carpeta de la skill a tu directorio de skills de usuario:

```bash
# desde una copia de este repo
mkdir -p ~/.claude/skills/upload-transcript
cp skills/upload-transcript/SKILL.md ~/.claude/skills/upload-transcript/SKILL.md
```

En Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force ~/.claude/skills/upload-transcript
Copy-Item skills/upload-transcript/SKILL.md ~/.claude/skills/upload-transcript/SKILL.md
```

Reiniciá Claude Code para que la detecte.

## Uso

- Pegá la transcript en el chat y decí *"subí esta transcript"* / *"cargala al
  repo Transcripts"*, **o**
- Invocá `/upload-transcript` directamente, **o**
- (Con Apollo conectado) pedí *"traé la transcript de <reunión> de Apollo y
  cargala"*.

## Convenciones

- Un archivo por transcript. Nombre `YYYY-MM-DD-empresa.md` cuando se conoce la
  fecha (Apollo la trae); si no, `empresa-contraparte.md`.
- Nunca se inventan fechas, nombres, citas ni números que no estén en la fuente.
- El `stage` en Attio se cambia solo cuando la señal es inequívoca; ante la duda,
  la skill sugiere y no toca.
