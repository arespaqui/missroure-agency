const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  LevelFormat, Header, Footer, PageNumber
} = require('/tmp/npm_global/lib/node_modules/docx');
const fs = require('fs');

const ROSA = "C4788A";
const GRIS = "4A4A4A";
const GRIS_CLARO = "F5F5F5";
const BLANCO = "FFFFFF";
const b = { style: BorderStyle.SINGLE, size: 1, color: "D9C4CB" };
const borders = { top: b, bottom: b, left: b, right: b };

function h1(t) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 120 },
    children: [new TextRun({ text: t, bold: true, size: 30, color: ROSA, font: "Arial" })] });
}
function h2(t) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 80 },
    children: [new TextRun({ text: t, bold: true, size: 24, color: "6B3A4A", font: "Arial" })] });
}
function h3(t) {
  return new Paragraph({ spacing: { before: 160, after: 60 },
    children: [new TextRun({ text: t, bold: true, size: 22, color: GRIS, font: "Arial" })] });
}
function p(t) {
  return new Paragraph({ spacing: { after: 100 },
    children: [new TextRun({ text: t, size: 20, font: "Arial" })] });
}
function bullet(t) {
  return new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 60 },
    children: [new TextRun({ text: t, size: 20, font: "Arial" })] });
}
function divider() {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "E8B4C8", space: 1 } },
    spacing: { before: 160, after: 160 }, children: [] });
}
function spacer() { return new Paragraph({ spacing: { after: 120 }, children: [] }); }

function tbl(headers, rows, cols) {
  const total = cols.reduce((a,x) => a+x, 0);
  return new Table({
    width: { size: total, type: WidthType.DXA },
    columnWidths: cols,
    rows: [
      new TableRow({ tableHeader: true,
        children: headers.map((h, i) => new TableCell({
          borders, width: { size: cols[i], type: WidthType.DXA },
          shading: { fill: "9E3A5A", type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: h, bold: true, size: 18, color: BLANCO, font: "Arial" })] })]
        }))
      }),
      ...rows.map((row, ri) => new TableRow({
        children: row.map((cell, i) => new TableCell({
          borders, width: { size: cols[i], type: WidthType.DXA },
          shading: { fill: ri % 2 === 0 ? GRIS_CLARO : BLANCO, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: cell, size: 18, font: "Arial" })] })]
        }))
      }))
    ]
  });
}

function box(t) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [9360],
    rows: [new TableRow({ children: [new TableCell({
      borders: {
        top: { style: BorderStyle.SINGLE, size: 6, color: ROSA },
        bottom: { style: BorderStyle.SINGLE, size: 6, color: ROSA },
        left: { style: BorderStyle.SINGLE, size: 6, color: ROSA },
        right: { style: BorderStyle.SINGLE, size: 6, color: ROSA }
      },
      shading: { fill: "FFF0F5", type: ShadingType.CLEAR },
      margins: { top: 120, bottom: 120, left: 180, right: 180 },
      children: [new Paragraph({ children: [new TextRun({ text: t, size: 20, font: "Arial", italics: true, color: "5C2D3A" })] })]
    })] })]
  });
}

const doc = new Document({
  numbering: { config: [{ reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }] },
  styles: {
    default: { document: { run: { font: "Arial", size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 30, bold: true, font: "Arial", color: ROSA }, paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: "Arial", color: "6B3A4A" }, paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "E8B4C8", space: 1 } }, children: [new TextRun({ text: "ROURE | Informe de Contenido Mayo 2026", size: 16, color: ROSA, font: "Arial", italics: true })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 4, color: "E8B4C8", space: 1 } }, children: [new TextRun({ text: "roure.tiendanegocio.com  |  @missroure  |  Pag. ", size: 16, color: "999999", font: "Arial" }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "999999", font: "Arial" })] })] }) },
    children: [

      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 720, after: 120 }, children: [new TextRun({ text: "ROURE", bold: true, size: 72, color: ROSA, font: "Arial" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "Romantic life starts in your closet", size: 24, color: "999999", font: "Arial", italics: true })] }),
      divider(),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "INFORME DE CONTENIDO MENSUAL", bold: true, size: 32, color: GRIS, font: "Arial" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "27 de abril - 24 de mayo de 2026", size: 22, color: "777777", font: "Arial" })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 480 }, children: [new TextRun({ text: "Temporada Invierno 2026  |  @missroure", size: 20, color: ROSA, font: "Arial" })] }),
      spacer(),

      h1("1. Contexto y Objetivos del Mes"),
      p("Roure es una marca 100% digital con sede en Buenos Aires, orientada a mujeres de 18-35 anos. El objetivo de este periodo fue consolidar la presencia digital en transicion a Invierno 2026, priorizando:"),
      spacer(),
      bullet("Clicks al link en bio / trafico a roure.tiendanegocio.com"),
      bullet("Cuentas alcanzadas nuevas y seguidores ganados"),
      bullet("Guardados (senal de intencion de compra)"),
      bullet("Comentarios con consultas por producto"),
      spacer(),
      box("Roure no empuja, seduce. La conexion emocional primero; la compra es consecuencia."),
      spacer(),
      divider(),

      h1("2. Estado Actual del Perfil (23 de mayo de 2026)"),
      spacer(),
      tbl(["Metrica", "Instagram", "TikTok"], [
        ["Seguidores", "677 (+36.8% desde abr 2022)", "677"],
        ["Publicaciones / Videos", "42 publicaciones", "Activo - multiples videos del periodo"],
        ["Link en bio", "roure.tiendanegocio.com", "Pendiente configurar"],
        ["Highlights activos", "Envios / Maquillaje / Ref Miss Roure / Ingresos", "N/A"],
      ], [3000, 3180, 3180]),
      spacer(),
      divider(),

      h1("3. Metricas del Periodo - Datos Reales"),
      spacer(),

      h2("3.1 TikTok @missroure (25 abr - 22 may 2026)"),
      p("Resumen de TikTok Analytics del periodo de 28 dias:"),
      spacer(),
      tbl(["Metrica", "Valor", "Variacion vs periodo anterior"], [
        ["Visualizaciones de videos", "15,000", "+12K (+410%)"],
        ["Visualizaciones de perfil", "600", "+475 (+380%)"],
        ["Me gusta", "868", "+744 (+600%)"],
        ["Comentarios", "12", "+12 (de 0 a 12)"],
        ["Veces compartido", "97", "+66 (+212.9%)"],
        ["Seguidores netos ganados", "+182", "Crecimiento muy fuerte para la etapa"],
      ], [2800, 2200, 4360]),
      spacer(),
      box("Todos los indicadores de TikTok crecieron entre +210% y +600% respecto al periodo anterior. El contenido empezo a funcionar."),
      spacer(),
      h3("Fuentes de trafico TikTok:"),
      tbl(["Fuente", "%", "Lectura"], [
        ["Para ti (FYP)", "76.1%", "El algoritmo distribuye activamente - senal excelente"],
        ["Perfil personal", "17.5%", "Audiencia fiel que vuelve al perfil"],
        ["Buscar", "4.7%", "Oportunidad: mejorar hashtags para busqueda organica"],
        ["Siguiendo", "1.7%", "Bajo - los seguidores no siempre ven el contenido"],
        ["Sonido", "0.0%", "No se capitaliza audio trending - accion inmediata disponible"],
      ], [2200, 900, 6260]),
      spacer(),
      h3("Consultas de busqueda que llevaron a @missroure:"),
      bullet("sweater invierno / Chompa de osos cafe"),
      bullet("conjunto algodon con lycra flores"),
      bullet("off shoulder peru 2026"),
      bullet("bibi ropa"),
      spacer(),
      p("Insight: hay demanda activa de sweaters/chompas invierno y off-shoulder. El contenido esta alineado con esas busquedas pero puede profundizarse con mas descripciones de producto en captions."),
      spacer(),
      h3("Top 5 videos TikTok por nuevos seguidores ganados:"),
      tbl(["Pos.", "Titulo / Hook", "Nuevos seguidores", "Fecha"], [
        ["1", "Volvieron nuestros sweaters mas virales (estrella burdeo)", "86", "hace 2 sem."],
        ["2", "Hay algo mejor que el olor a hojas secas y el primer dia que...", "69", "4 abr"],
        ["3", "Reme Crop 3 x $24000", "55", "4 feb"],
        ["4", "Ya tienes tu sweater favorito para invierno? El Sweater Vien...", "47", "hace 3 sem."],
        ["5", "Holi Miss, el Sweater Vienne esta disponible en 4 colores", "14", "hace 2 sem."],
      ], [600, 4560, 1800, 2400]),
      spacer(),
      h3("Top 5 videos TikTok por nuevos espectadores alcanzados:"),
      tbl(["Pos.", "Titulo / Hook", "Nuevos espectadores", "Fecha"], [
        ["1", "Ya tienes tu sweater favorito para invierno? El Sweater Vien...", "2,090", "hace 3 sem."],
        ["2", "Volvieron nuestros sweaters mas virales", "1,845", "hace 2 sem."],
        ["3", "Hay algo mejor que el olor a hojas secas y el primer dia que...", "1,452", "4 abr"],
        ["4", "Reme Crop 3 x $24000", "781", "4 feb"],
        ["5", "Holi Miss, el Sweater Vienne en 4 colores", "691", "hace 2 sem."],
      ], [600, 4560, 2000, 2200]),
      spacer(),

      h2("3.2 Instagram @missroure (27 abr - 23 may 2026)"),
      tbl(["Metrica", "Valor", "Lectura"], [
        ["Cuentas alcanzadas (30 dias)", "480", "Mayormente seguidores - necesita ampliar alcance nuevo"],
        ["Visualizaciones publicaciones", "~1,500", "Publicaciones: formato con mas alcance del periodo"],
        ["Visualizaciones historias", "~1,200", "Muy activas - segunda fuente de visualizaciones"],
        ["Visualizaciones reels", "571", "Menor alcance siendo el formato mas potenciado - oportunidad critica"],
        ["Interacciones totales", "110", "Engagement moderado para la base actual"],
        ["Mix: seguidores vs no seguidores", "65.5% / 34.5%", "Buena proporcion llegando a cuentas nuevas"],
        ["Seguidores totales", "677", "+36.8% desde abril 2022"],
      ], [2800, 2200, 4360]),
      spacer(),
      h3("Top contenido Instagram por cuentas alcanzadas:"),
      tbl(["Contenido", "Cuentas alcanzadas", "Likes"], [
        ["Encontraste el off-shoulder perfecto...", "195", "8"],
        ["Amamos preparar cada paquete porque...", "108", "3"],
        ["Volvieron nuestros sweaters mas virales", "90", "5"],
        ["Restock Sweater Vienne + new Ingresos", "48", "1"],
        ["Aprecien los botones dorados en fo...", "41", "7"],
      ], [4360, 2500, 2500]),
      spacer(),
      box("Dato pendiente para el proximo informe: clicks al link en bio y guardados por post. Capturalos desde Instagram Insights > Actividad > Clics en enlace."),
      spacer(),

      h2("3.3 Diagnostico cruzado IG + TikTok"),
      bullet("HEROE del mes: el sweater burdeo con estrella funciono en TikTok (86 nuevos seguidores, 1,845 espectadores) y en Instagram (90 cuentas alcanzadas). Es el producto con mayor potencial de contenido para invierno."),
      bullet("Los hooks tipo pregunta emocional ('Hay algo mejor que el olor a hojas secas...') son los que mas seguidores nuevos generan - este formato hay que replicar sistematicamente."),
      bullet("TikTok crece explosivamente (+410% visualizaciones) pero Instagram sigue siendo la base de comunidad. Estrategia para ambas en paralelo."),
      bullet("El precio directo en caption (Reme Crop 3x$24000) convierte en seguidores nuevos - no hay que esconder los precios."),
      bullet("Los reels de Instagram tienen el menor alcance (571) siendo el formato mas potente del algoritmo. Mejorar hook en los primeros 2 segundos y agregar audio trending."),
      spacer(),
      divider(),

      h1("4. Benchmark de Inspiracion - Semana 19-23 Mayo 2026"),
      p("Analisis de cuentas de referencia: formatos, hooks y estructuras narrativas aplicables al niche de indumentaria femenina romantica para ecommerce argentino."),
      spacer(),

      h2("4.1 Teddystudio.bkk - 28.8K seg. / Bangkok / Ropa comoda cute"),
      tbl(["Fecha", "Formato", "Likes", "Hook principal", "Estructura narrativa"], [
        ["20 may", "Carrusel", "500", "Loviebear Collection is almost sold out!", "Urgencia de stock + precio especial final + sin restock"],
        ["22 may", "Carrusel", "74", "Your cozy wishlist starts here", "Catalogo en liquidacion + sin restock"],
        ["13 may", "Carrusel", "82", "New colors - wear as matching set or mix & match", "Nuevos colores + versatilidad + lifestyle cozy"],
        ["5 may", "Carrusel", "66", "New colors just dropped + Flash Sale 18:00-24:00", "Lanzamiento de color + urgencia de hora exacta"],
        ["18 may", "Carrusel", "n/d", "Flash Sale tonight 9PM + 20% extra codigo Shopee", "Doble urgencia: hora + descuento adicional de plataforma"],
      ], [900, 1100, 700, 2800, 3860]),
      spacer(),
      h3("Patrones aplicables a Roure:"),
      bullet("'Sin restock' como copy de urgencia: suave pero efectivo. No empuja, informa."),
      bullet("Flash Sale con hora exacta: crea habito de seguimiento en la audiencia."),
      bullet("Matching set como propuesta visual: simplifica la decision de compra, sube el ticket promedio."),
      spacer(),

      h2("4.2 Sugar & Spice - 171K seg. / Vietnam / Ropa handmade romantica"),
      tbl(["Fecha", "Formato", "Likes", "Hook principal", "Estructura narrativa"], [
        ["23 may", "Reel", "805", "aren't clothes supposed to make u feel comfy?", "Pregunta retorica emocional + vestido Empire Waist"],
        ["21 may", "Reel", "803", "pink + brown is something", "Combo de colores como protagonista + reaccion emocional"],
        ["13 may", "Reel", "1,400", "(sin copy - solo visual)", "Visual puro: cesta, luz dorada, estetica rural romantica"],
        ["10 may", "Carrusel", "270", "Vera Top - made with love, from heaven", "Nombre propio del producto + claim emocional minimalista"],
        ["10 may", "Carrusel", "n/d", "Fotos del mismo modelo en distintos angulos", "Catalogo visual sin copy extenso"],
      ], [900, 1100, 700, 2800, 3860]),
      spacer(),
      h3("Patrones aplicables a Roure:"),
      bullet("El reel de 805 likes valida la identidad de la clienta, no vende la prenda. Esto es el ADN de Roure."),
      bullet("El reel de 1,400 likes no tiene copy. El visual lo es todo. Roure puede y debe apostar a esto."),
      bullet("Nombres propios para prendas ('Vera Top'): generan memorabilidad y se piden por nombre en DM."),
      spacer(),

      h2("4.3 LoveShack Fancy - +1M seg. / EE.UU. / Moda romantica premium"),
      tbl(["Fecha", "Formato", "Engagement", "Hook principal", "Estructura narrativa"], [
        ["23 may", "Carrusel", "9+ likes", "Summer is our homecoming - el arbol donde empezo todo...", "Storytelling de origen de marca: boda, jardin, inicio de LSF"],
        ["23 may", "Reel", "17+ likes", "You heard it here first - The American Road Trip Cotton Collection", "Collab con musa + producto con nombre propio memorable"],
        ["22 may", "Reel", "16+ likes", "Running through the garden in the dress inspired by our forever Love Dress", "Lifestyle visual: descalza, jardin, hora dorada, flores"],
        ["23 may", "Reel", "n/d", "Our muse looking stunning in...", "Formato musa: persona aspiracional + prenda + contexto sonado"],
        ["21 may", "Carrusel", "n/d", "Coleccion floral para bodas", "Editorial invitada de boda + inclusividad de tallas (mid-size)"],
      ], [900, 1100, 1300, 2500, 3560]),
      spacer(),
      h3("Patrones aplicables a Roure:"),
      bullet("Storytelling de marca: cada post es un capitulo de la historia de LSF. Roure puede hacer lo mismo."),
      bullet("La pergola de flores como simbolo recurrente. Roure puede construir su propio simbolo visual (el placard, el espejo, una taza de cafe)."),
      bullet("Nombrar productos con personalidad: 'Love Dress'. En Roure el 'Sweater Estrella' ya funciona - expandir eso."),
      spacer(),

      h2("4.4 Lulus - 2.4M seg. / EE.UU. / Moda femenina accesible e inclusiva"),
      tbl(["Fecha", "Formato", "Likes", "Hook principal", "Estructura narrativa"], [
        ["23 may", "Reel", "33", "no need to fight over the bouquet toss when these dresses look this gorgeous", "Humor situacional + producto + CTA al link en bio"],
        ["23 may", "Reel", "3", "Stylist Series: head stylist spills expert tips + summer arrivals", "Serie educativa serializada + producto + engagement habitual"],
        ["22 may", "Reel", "16", "What happens in Vegas stays there - curvy party dresses", "Humor cultural + musa curvy + ocasion de uso especifica"],
        ["Todos", "Todos", "---", "tap the link in our bio to shop", "CTA al link en bio como cierre de absolutamente TODOS los posts"],
        ["Todas", "Todas", "---", "#lovelulus", "Hashtag de marca propio en cada publicacion para UGC organico"],
      ], [900, 1100, 700, 2800, 3860]),
      spacer(),
      h3("Patrones aplicables a Roure:"),
      bullet("CTA al link en bio en TODOS los posts - sin excepcion, sin verguenza. Lulus tiene 2.4M y lo hace igual."),
      bullet("'Stylist Series': contenido educativo serializado que da razon para volver semana a semana."),
      bullet("Hashtag propio (#missroure o #rourelife) en cada publicacion para construir UGC organico."),
      spacer(),
      divider(),

      h1("5. Sintesis Estrategica - Que Esta Funcionando y Que No"),
      spacer(),
      h2("5.1 Lo que ya esta funcionando"),
      bullet("Hooks de pregunta emocional: 'Hay algo mejor que el olor a hojas secas...' genera 69+ nuevos seguidores en un solo video. Exactamente lo que hacen las cuentas de referencia."),
      bullet("El Sweater Estrella burdeo: producto heroe que funciona en ambas plataformas. Hay que seguir mostrando prendas con identidad visual fuerte."),
      bullet("Precio directo en caption (3x$24000): convierte en seguidores nuevos. No hay que esconder los precios."),
      bullet("TikTok con FYP activo al 76%: el algoritmo ya distribuye el contenido. Momento de mas gas, no de menos."),
      spacer(),
      h2("5.2 Lo que necesita cambiar"),
      bullet("Reels de Instagram: menor alcance (571) siendo el formato mas potenciado por el algoritmo. Mejorar el hook en los primeros 2 segundos."),
      bullet("Audio en TikTok: 0% de trafico por sonido. Un solo reel con audio viral puede multiplicar el alcance por 10."),
      bullet("CTA al link en bio: no aparece en todas las publicaciones. Debe ser rutina no negociable."),
      bullet("Guardados: implementar carruseles 'como combinarlo' que activan guardados de forma natural."),
      spacer(),
      h2("5.3 Hooks recomendados para Roure Invierno 2026"),
      tbl(["Tipo de hook", "Ejemplo del benchmark", "Version para Roure"], [
        ["Pregunta retorica emocional", "aren't clothes supposed to make u feel comfy?", "Y si tu outfit del lunes empezara a sentirse como un abrazo?"],
        ["Emocion sobre el color", "pink + brown is something", "El burdeo de este invierno va a hacer cosas contigo"],
        ["Urgencia suave de stock", "last pieces - won't be restocked", "Ultimas unidades del cardigan crema. No repone."],
        ["Nombre propio del producto", "Vera Top - made with love, from heaven", "Cardigan Luna. Para los dias que necesitas envolverte en algo tuyo."],
        ["Precio directo como hook", "Reme Crop 3 x $24000", "3 sweaters por $X. El invierno no espera."],
        ["Visual puro sin copy", "(solo estetica + musica)", "Prenda en interior calido, luz natural, sin texto."],
      ], [2100, 3000, 4260]),
      spacer(),
      divider(),

      h1("6. Recomendaciones para Junio 2026"),
      spacer(),
      h2("Prioridad 1 - Trafico a la tienda (el norte)"),
      bullet("CTA al link en bio en TODOS los posts y reels - sin excepcion."),
      bullet("En reels: terminar SIEMPRE con nombre del producto + 'link en bio para llevartelo'."),
      bullet("Crear Highlight 'Tienda' en Instagram con acceso directo a roure.tiendanegocio.com."),
      bullet("En TikTok: usar el boton 'Agregar enlace' en cada video para ir directamente a la tienda."),
      spacer(),
      h2("Prioridad 2 - Contenido de alta intencion de guardado"),
      bullet("Carruseles 'una prenda, 3 outfits': el formato con mas guardados en todo el niche."),
      bullet("'Wishlist de invierno': moodboard digital con las prendas de la temporada."),
      bullet("Nombrar cada prenda: 'Cardigan Luna', 'Buzo Aurora', 'Sweater Estrella'. El nombre hace que se pida por nombre en DM."),
      spacer(),
      h2("Prioridad 3 - Crecer en alcance nuevo"),
      bullet("1 reel por semana con hook emocional en el primer segundo en Instagram."),
      bullet("En TikTok: incorporar 1 audio trending por semana que encaje con la estetica romantica. Esto puede multiplicar el alcance inmediatamente."),
      bullet("Responder a TODOS los comentarios dentro de las primeras 2 horas de publicado. El algoritmo lo premia."),
      spacer(),
      h2("Prioridad 4 - Consultas y engagement de compra"),
      bullet("Stories interactivas 'Este o este' con dos prendas - genera DMs y mide preferencia real."),
      bullet("'Ultimas X unidades' cuando sea real, con prueba en stories (mostrar el stock fisicamente)."),
      bullet("Preguntas abiertas en el caption: 'Con que lo combinarias vos?' - activan comentarios organicos."),
      bullet("Responder SIEMPRE preguntas por precio o disponibilidad en comentarios - son las consultas de mayor valor."),
      spacer(),
      divider(),

      h1("7. Proximos Pasos Concretos"),
      tbl(["Accion", "Plazo", "Responsable"], [
        ["Grabar 1 reel con hook emocional tipo pregunta (ej: 'Y si tu outfit de manana...')", "Esta semana", "Roure"],
        ["Agregar audio trending de TikTok a 1 video nuevo", "Esta semana", "Roure"],
        ["Actualizar Highlight 'Tienda' con link directo a roure.tiendanegocio.com", "Esta semana", "Roure"],
        ["Nombrar todas las prendas de invierno 2026 con nombres propios", "Esta semana", "Roure"],
        ["Crear 1 carrusel 'una prenda, 3 outfits' con prenda de invierno", "Proxima semana", "Roure"],
        ["Activar CTA al link en bio en TODOS los proximos posts", "Inmediato y permanente", "Roure"],
        ["Capturar datos de clicks al link en bio y guardados para proximo informe", "Al cierre de junio", "Roure"],
        ["Armar calendario de contenido de junio con formatos validados", "Proxima semana", "Roure"],
      ], [4000, 2000, 3360]),
      spacer(),
      spacer(),
      box("Roure no necesita mas volumen de publicaciones - necesita que cada post cumpla una funcion especifica. Menos, pero con proposito. Eso es lo que convierte."),
      spacer(),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 480, after: 60 }, children: [new TextRun({ text: "Informe preparado con Claude - Cowork Mode", size: 16, color: "BBBBBB", font: "Arial", italics: true })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "missroure  |  roure.tiendanegocio.com  |  Mayo 2026", size: 16, color: "BBBBBB", font: "Arial" })] }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/sessions/vigilant-optimistic-pascal/mnt/missroure-agency/Roure_Informe_Contenido_Mayo2026.docx", buffer);
  console.log("OK");
}).catch(e => { console.error(e.message); process.exit(1); });
