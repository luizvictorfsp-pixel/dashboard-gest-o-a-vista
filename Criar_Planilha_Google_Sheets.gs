/**
 * GOOGLE APPS SCRIPT: CRIADOR AUTOMÁTICO DA PLANILHA GESTÃO À VISTA
 * 
 * Como usar:
 * 1. Acesse https://script.new (ou abra o Google Drive e crie um Google Apps Script)
 * 2. Substitua todo o conteúdo pelo código abaixo
 * 3. Clique em "Executar" (ícone de Play ▶)
 * 4. Autorize a execução na sua conta Google
 * 5. Veja no Registro de Execução o ID e a URL gerada para usar no Dashboard!
 */

function criarPlanilhaGestaoAVista() {
  const nomePlanilha = "Gestão a Vista — DNA Facilities (Dados Oficiais)";
  const ss = SpreadsheetApp.create(nomePlanilha);
  
  Logger.log("Criando planilha: " + nomePlanilha);
  
  // Dados de cada aba
  const abas = [
    {
      nome: "RH",
      cor: "#0284c7",
      cabecalho: ["MES", "EFETIVO_CONTRATUAL", "EFETIVO_REALIZADO", "ADMISSOES", "DESLIGAMENTOS", "AFASTAMENTO", "FERIAS", "HORAS_PREVISTAS", "HORAS_AUSENCIA"],
      linhas: [
        ["Jan/26", 130, 120, 4, 2, 3, 5, 21600, 432],
        ["Fev/26", 130, 122, 3, 1, 2, 6, 20740, 311],
        ["Mar/26", 130, 125, 5, 2, 4, 4, 22500, 562],
        ["Abr/26", 130, 124, 2, 3, 3, 5, 21080, 421],
        ["Mai/26", 130, 126, 4, 2, 2, 7, 21420, 321],
        ["Jun/26", 130, 128, 3, 1, 1, 6, 23040, 345],
        ["Jul/26", 130, 127, 2, 3, 2, 4, 22860, 457],
        ["Ago/26", 130, 129, 4, 2, 3, 3, 23220, 290],
        ["Set/26", 130, 130, 2, 1, 1, 5, 23400, 234],
        ["Out/26", 130, 128, 3, 2, 2, 6, 21760, 370]
      ]
    },
    {
      nome: "SMA",
      cor: "#d97706",
      cabecalho: ["MES", "HHT", "ACIDENTES_COM_AFASTAMENTO", "ACIDENTES_SEM_AFASTAMENTO", "ACIDENTES_TRAJETO", "INSPECOES_PLANEJADAS", "INSPECOES_REALIZADAS", "DESVIOS_REGISTRADOS", "DESVIOS_TRATADOS"],
      linhas: [
        ["Jan/26", 21600, 0, 0, 0, 10, 10, 2, 2],
        ["Fev/26", 20740, 0, 1, 0, 10, 9, 3, 3],
        ["Mar/26", 22500, 0, 0, 1, 12, 12, 1, 1],
        ["Abr/26", 21080, 0, 0, 0, 10, 10, 4, 3],
        ["Mai/26", 21420, 0, 0, 0, 10, 10, 2, 2],
        ["Jun/26", 23040, 0, 1, 0, 12, 11, 3, 3],
        ["Jul/26", 22860, 1, 0, 0, 10, 10, 5, 4],
        ["Ago/26", 23220, 0, 0, 0, 12, 12, 2, 2],
        ["Set/26", 23400, 0, 1, 0, 10, 10, 3, 2],
        ["Out/26", 21760, 0, 0, 0, 10, 9, 4, 4]
      ]
    },
    {
      nome: "Orcamento",
      cor: "#7c3aed",
      cabecalho: ["MES", "CATEGORIA", "ORCADO", "REALIZADO", "CENTRO_CUSTO", "UF"],
      linhas: [
        ["Jan/26", "Mão de Obra e Encargos", 180000, 178500, "CC-101", "SP"],
        ["Jan/26", "Benefícios (VT/VR/VA)", 35000, 36200, "CC-101", "SP"],
        ["Jan/26", "Insumos e Químicos", 12000, 11400, "CC-101", "SP"],
        ["Jan/26", "Uniformes e EPIs", 6000, 6800, "CC-101", "SP"],
        ["Jan/26", "Equipamentos", 15000, 15000, "CC-101", "SP"],
        ["Fev/26", "Mão de Obra e Encargos", 180000, 177200, "CC-101", "SP"],
        ["Fev/26", "Benefícios (VT/VR/VA)", 35000, 34800, "CC-101", "SP"],
        ["Fev/26", "Insumos e Químicos", 12000, 12600, "CC-101", "SP"],
        ["Fev/26", "Uniformes e EPIs", 6000, 5900, "CC-101", "SP"],
        ["Fev/26", "Equipamentos", 15000, 14500, "CC-101", "SP"],
        ["Mar/26", "Mão de Obra e Encargos", 180000, 181000, "CC-101", "SP"],
        ["Mar/26", "Benefícios (VT/VR/VA)", 35000, 35500, "CC-101", "SP"],
        ["Mar/26", "Insumos e Químicos", 12000, 11800, "CC-101", "SP"],
        ["Mar/26", "Uniformes e EPIs", 6000, 5800, "CC-101", "SP"],
        ["Mar/26", "Equipamentos", 15000, 16200, "CC-101", "SP"],
        ["Abr/26", "Mão de Obra e Encargos", 180000, 179000, "CC-101", "SP"],
        ["Abr/26", "Benefícios (VT/VR/VA)", 35000, 35100, "CC-101", "SP"],
        ["Abr/26", "Insumos e Químicos", 12000, 12300, "CC-101", "SP"],
        ["Abr/26", "Uniformes e EPIs", 6000, 5500, "CC-101", "SP"],
        ["Abr/26", "Equipamentos", 15000, 14800, "CC-101", "SP"],
        ["Mai/26", "Mão de Obra e Encargos", 180000, 176400, "CC-101", "SP"],
        ["Mai/26", "Benefícios (VT/VR/VA)", 35000, 36100, "CC-101", "SP"],
        ["Mai/26", "Insumos e Químicos", 12000, 11200, "CC-101", "SP"],
        ["Mai/26", "Uniformes e EPIs", 6000, 6400, "CC-101", "SP"],
        ["Mai/26", "Equipamentos", 15000, 15000, "CC-101", "SP"],
        ["Jun/26", "Mão de Obra e Encargos", 180000, 180500, "CC-101", "SP"],
        ["Jun/26", "Benefícios (VT/VR/VA)", 35000, 34900, "CC-101", "SP"],
        ["Jun/26", "Insumos e Químicos", 12000, 12100, "CC-101", "SP"],
        ["Jun/26", "Uniformes e EPIs", 6000, 6200, "CC-101", "SP"],
        ["Jun/26", "Equipamentos", 15000, 15500, "CC-101", "SP"]
      ]
    },
    {
      nome: "Medicao",
      cor: "#059669",
      cabecalho: ["COMPETENCIA", "CONTRATO", "VALOR_CONTRATUAL", "VALOR_MEDIDO", "VALOR_APROVADO", "VALOR_GLOSAS", "MOTIVO_GLOSA", "VALOR_FATURADO", "VALOR_RECEBIDO", "STATUS", "DATA_SUBMISSAO"],
      linhas: [
        ["2026-01", "CT-2024-HOSP", 350000, 350000, 349000, 1000, "Atraso em ponto", 349000, 349000, "recebido", "02/02/2026"],
        ["2026-02", "CT-2024-HOSP", 350000, 350000, 350000, 0, "", 350000, 350000, "recebido", "03/03/2026"],
        ["2026-03", "CT-2024-HOSP", 350000, 350000, 348500, 1500, "Posto noturno", 348500, 348500, "recebido", "02/04/2026"],
        ["2026-04", "CT-2024-HOSP", 350000, 350000, 350000, 0, "", 350000, 350000, "recebido", "02/05/2026"],
        ["2026-05", "CT-2024-HOSP", 350000, 350000, 348200, 1800, "Posto pontual", 348200, 348200, "recebido", "02/06/2026"],
        ["2026-06", "CT-2024-HOSP", 350000, 350000, 350000, 0, "", 350000, 350000, "recebido", "03/07/2026"],
        ["2026-07", "CT-2024-HOSP", 350000, 350000, 347500, 2500, "Cronograma", 347500, 347500, "recebido", "04/08/2026"],
        ["2026-08", "CT-2024-HOSP", 350000, 350000, 350000, 0, "", 350000, 350000, "recebido", "02/09/2026"],
        ["2026-09", "CT-2024-HOSP", 350000, 350000, 350000, 0, "", 350000, 0, "faturado", "02/10/2026"],
        ["2026-10", "CT-2024-HOSP", 350000, 350000, 0, 0, "", 0, 0, "submetido", "16/10/2026"]
      ]
    }
  ];

  const defaultSheet = ss.getSheets()[0];

  abas.forEach((aba, idx) => {
    let sheet;
    if (idx === 0) {
      sheet = defaultSheet;
      sheet.setName(aba.nome);
    } else {
      sheet = ss.insertSheet(aba.nome);
    }
    
    sheet.setTabColor(aba.cor);
    sheet.setFrozenRows(1);

    // Inserir cabeçalho
    const headerRange = sheet.getRange(1, 1, 1, aba.cabecalho.length);
    headerRange.setValues([aba.cabecalho]);
    headerRange.setBackground("#1e293b");
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setFontSize(10);
    headerRange.setHorizontalAlignment("center");

    // Inserir linhas
    if (aba.linhas.length > 0) {
      const dataRange = sheet.getRange(2, 1, aba.linhas.length, aba.cabecalho.length);
      dataRange.setValues(aba.linhas);
      dataRange.setFontSize(10);
      dataRange.setVerticalAlignment("middle");

      // Formatação condicional e alternância de cores
      for (let r = 0; r < aba.linhas.length; r++) {
        const rowRange = sheet.getRange(r + 2, 1, 1, aba.cabecalho.length);
        if (r % 2 === 1) {
          rowRange.setBackground("#f8fafc");
        }
      }
    }

    // Auto-ajuste de colunas
    for (let c = 1; c <= aba.cabecalho.length; c++) {
      sheet.autoResizeColumn(c);
      const w = sheet.getColumnWidth(c);
      sheet.setColumnWidth(c, Math.max(w + 20, 110));
    }
  });

  const url = ss.getUrl();
  const id = ss.getId();

  Logger.log("=================================================");
  Logger.log("✅ PLANILHA CRIADA COM SUCESSO!");
  Logger.log("🔗 URL da Planilha: " + url);
  Logger.log("🆔 ID do Google Sheets: " + id);
  Logger.log("=================================================");
  Logger.log("Próximos passos:");
  Logger.log("1. No menu da planilha: Arquivo > Compartilhar > Publicar na Web > Publicar");
  Logger.log("2. Copie o ID acima e cole no campo do Dashboard.");
}
