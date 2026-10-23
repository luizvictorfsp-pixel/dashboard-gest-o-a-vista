import os
import csv
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

base_dir = r"C:\Antigravity\docs"
sheets_dir = os.path.join(base_dir, "planilha-google-sheets")
os.makedirs(sheets_dir, exist_ok=True)

# 1. DATA DEFINITIONS
rh_headers = [
    "MES", "EFETIVO_CONTRATUAL", "EFETIVO_REALIZADO", "ADMISSOES",
    "DESLIGAMENTOS", "AFASTAMENTO", "FERIAS", "HORAS_PREVISTAS", "HORAS_AUSENCIA"
]
rh_rows = [
    ["Jan/26", 130, 120, 4, 2, 3, 5, 21600, 432],
    ["Fev/26", 130, 122, 3, 1, 2, 6, 20740, 311],
    ["Mar/26", 130, 125, 5, 2, 4, 4, 22500, 562],
    ["Abr/26", 130, 124, 2, 3, 3, 5, 21080, 421],
    ["Mai/26", 130, 126, 4, 2, 2, 7, 21420, 321],
    ["Jun/26", 130, 128, 3, 1, 1, 6, 23040, 345],
    ["Jul/26", 130, 127, 2, 3, 2, 4, 22860, 457],
    ["Ago/26", 130, 129, 4, 2, 3, 3, 23220, 290],
    ["Set/26", 130, 130, 2, 1, 1, 5, 23400, 234],
    ["Out/26", 130, 128, 3, 2, 2, 6, 21760, 370],
]

sma_headers = [
    "MES", "HHT", "ACIDENTES_COM_AFASTAMENTO", "ACIDENTES_SEM_AFASTAMENTO",
    "ACIDENTES_TRAJETO", "INSPECOES_PLANEJADAS", "INSPECOES_REALIZADAS",
    "DESVIOS_REGISTRADOS", "DESVIOS_TRATADOS"
]
sma_rows = [
    ["Jan/26", 21600, 0, 0, 0, 10, 10, 2, 2],
    ["Fev/26", 20740, 0, 1, 0, 10, 9, 3, 3],
    ["Mar/26", 22500, 0, 0, 1, 12, 12, 1, 1],
    ["Abr/26", 21080, 0, 0, 0, 10, 10, 4, 3],
    ["Mai/26", 21420, 0, 0, 0, 10, 10, 2, 2],
    ["Jun/26", 23040, 0, 1, 0, 12, 11, 3, 3],
    ["Jul/26", 22860, 1, 0, 0, 10, 10, 5, 4],
    ["Ago/26", 23220, 0, 0, 0, 12, 12, 2, 2],
    ["Set/26", 23400, 0, 1, 0, 10, 10, 3, 2],
    ["Out/26", 21760, 0, 0, 0, 10, 9, 4, 4],
]

orc_headers = ["MES", "CATEGORIA", "ORCADO", "REALIZADO", "CENTRO_CUSTO", "UF"]
orc_rows = [
    ["Jan/26", "Mão de Obra e Encargos", 180000.0, 178500.0, "CC-101", "SP"],
    ["Jan/26", "Benefícios (VT/VR/VA)", 35000.0, 36200.0, "CC-101", "SP"],
    ["Jan/26", "Insumos e Químicos", 12000.0, 11400.0, "CC-101", "SP"],
    ["Jan/26", "Uniformes e EPIs", 6000.0, 6800.0, "CC-101", "SP"],
    ["Jan/26", "Equipamentos", 15000.0, 15000.0, "CC-101", "SP"],
    ["Fev/26", "Mão de Obra e Encargos", 180000.0, 177200.0, "CC-101", "SP"],
    ["Fev/26", "Benefícios (VT/VR/VA)", 35000.0, 34800.0, "CC-101", "SP"],
    ["Fev/26", "Insumos e Químicos", 12000.0, 12600.0, "CC-101", "SP"],
    ["Fev/26", "Uniformes e EPIs", 6000.0, 5900.0, "CC-101", "SP"],
    ["Fev/26", "Equipamentos", 15000.0, 14500.0, "CC-101", "SP"],
    ["Mar/26", "Mão de Obra e Encargos", 180000.0, 181000.0, "CC-101", "SP"],
    ["Mar/26", "Benefícios (VT/VR/VA)", 35000.0, 35500.0, "CC-101", "SP"],
    ["Mar/26", "Insumos e Químicos", 12000.0, 11800.0, "CC-101", "SP"],
    ["Mar/26", "Uniformes e EPIs", 6000.0, 5800.0, "CC-101", "SP"],
    ["Mar/26", "Equipamentos", 15000.0, 16200.0, "CC-101", "SP"],
    ["Abr/26", "Mão de Obra e Encargos", 180000.0, 179000.0, "CC-101", "SP"],
    ["Abr/26", "Benefícios (VT/VR/VA)", 35000.0, 35100.0, "CC-101", "SP"],
    ["Abr/26", "Insumos e Químicos", 12000.0, 12300.0, "CC-101", "SP"],
    ["Abr/26", "Uniformes e EPIs", 6000.0, 5500.0, "CC-101", "SP"],
    ["Abr/26", "Equipamentos", 15000.0, 14800.0, "CC-101", "SP"],
    ["Mai/26", "Mão de Obra e Encargos", 180000.0, 176400.0, "CC-101", "SP"],
    ["Mai/26", "Benefícios (VT/VR/VA)", 35000.0, 36100.0, "CC-101", "SP"],
    ["Mai/26", "Insumos e Químicos", 12000.0, 11200.0, "CC-101", "SP"],
    ["Mai/26", "Uniformes e EPIs", 6000.0, 6400.0, "CC-101", "SP"],
    ["Mai/26", "Equipamentos", 15000.0, 15000.0, "CC-101", "SP"],
    ["Jun/26", "Mão de Obra e Encargos", 180000.0, 180500.0, "CC-101", "SP"],
    ["Jun/26", "Benefícios (VT/VR/VA)", 35000.0, 34900.0, "CC-101", "SP"],
    ["Jun/26", "Insumos e Químicos", 12000.0, 12100.0, "CC-101", "SP"],
    ["Jun/26", "Uniformes e EPIs", 6000.0, 6200.0, "CC-101", "SP"],
    ["Jun/26", "Equipamentos", 15000.0, 15500.0, "CC-101", "SP"],
]

med_headers = [
    "COMPETENCIA", "CONTRATO", "VALOR_CONTRATUAL", "VALOR_MEDIDO",
    "VALOR_APROVADO", "VALOR_GLOSAS", "MOTIVO_GLOSA", "VALOR_FATURADO",
    "VALOR_RECEBIDO", "STATUS", "DATA_SUBMISSAO"
]
med_rows = [
    ["2026-01", "CT-2024-HOSP", 350000.0, 350000.0, 349000.0, 1000.0, "Atraso em ponto", 349000.0, 349000.0, "recebido", "02/02/2026"],
    ["2026-02", "CT-2024-HOSP", 350000.0, 350000.0, 350000.0, 0.0, "", 350000.0, 350000.0, "recebido", "03/03/2026"],
    ["2026-03", "CT-2024-HOSP", 350000.0, 350000.0, 348500.0, 1500.0, "Posto noturno", 348500.0, 348500.0, "recebido", "02/04/2026"],
    ["2026-04", "CT-2024-HOSP", 350000.0, 350000.0, 350000.0, 0.0, "", 350000.0, 350000.0, "recebido", "02/05/2026"],
    ["2026-05", "CT-2024-HOSP", 350000.0, 350000.0, 348200.0, 1800.0, "Posto pontual", 348200.0, 348200.0, "recebido", "02/06/2026"],
    ["2026-06", "CT-2024-HOSP", 350000.0, 350000.0, 350000.0, 0.0, "", 350000.0, 350000.0, "recebido", "03/07/2026"],
    ["2026-07", "CT-2024-HOSP", 350000.0, 350000.0, 347500.0, 2500.0, "Cronograma", 347500.0, 347500.0, "recebido", "04/08/2026"],
    ["2026-08", "CT-2024-HOSP", 350000.0, 350000.0, 350000.0, 0.0, "", 350000.0, 350000.0, "recebido", "02/09/2026"],
    ["2026-09", "CT-2024-HOSP", 350000.0, 350000.0, 350000.0, 0.0, "", 350000.0, 0.0, "faturado", "02/10/2026"],
    ["2026-10", "CT-2024-HOSP", 350000.0, 350000.0, 0.0, 0.0, "", 0.0, 0.0, "submetido", "16/10/2026"],
]

sheets_data = {
    "RH": (rh_headers, rh_rows, "0284C7"),
    "SMA": (sma_headers, sma_rows, "D97706"),
    "Orcamento": (orc_headers, orc_rows, "7C3AED"),
    "Medicao": (med_headers, med_rows, "059669")
}

# 2. WRITE INDIVIDUAL CSV FILES
for tab_name, (headers, rows, _) in sheets_data.items():
    csv_path = os.path.join(sheets_dir, f"{tab_name}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Generated CSV: {csv_path}")

# 3. WRITE EXCEL WORKBOOK (.XLSX)
wb = openpyxl.Workbook()
# remove default sheet
wb.remove(wb.active)

thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

for tab_name, (headers, rows, tab_color) in sheets_data.items():
    ws = wb.create_sheet(title=tab_name)
    ws.sheet_properties.tabColor = tab_color
    ws.views.sheetView[0].showGridLines = True

    # Header styling
    header_fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
    header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws.row_dimensions[1].height = 28

    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_align
        cell.border = thin_border

    # Freeze top row
    ws.freeze_panes = "A2"

    # Row styling
    data_font = Font(name="Segoe UI", size=10, color="0F172A")
    even_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    odd_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    for row_idx, row_data in enumerate(rows, 2):
        ws.row_dimensions[row_idx].height = 20
        fill = even_fill if row_idx % 2 == 0 else odd_fill

        for col_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.font = data_font
            cell.fill = fill
            cell.border = thin_border

            # Number formatting
            header_name = headers[col_idx - 1]
            if isinstance(val, float) or "VALOR" in header_name or "ORCADO" in header_name or "REALIZADO" in header_name:
                cell.number_format = 'R$ #,##0.00'
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif isinstance(val, int):
                cell.number_format = '#,##0'
                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="center" if len(str(val)) <= 10 else "left", vertical="center")

    # Auto-adjust column widths
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or "")
            if len(val_str) > max_len:
                max_len = len(val_str)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 14)

excel_path = os.path.join(base_dir, "Planilha_Gestao_a_Vista_GoogleSheets.xlsx")
wb.save(excel_path)
print(f"Generated Excel: {excel_path}")
