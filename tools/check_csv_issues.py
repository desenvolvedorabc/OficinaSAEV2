#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_csv_issues.py
Script para análise de arquivos CSV com cabeçalho na primeira linha.

Funcionalidades:
- Verifica se o número de colunas em cada linha coincide com o cabeçalho.
- Detecta se campos string possuem o separador embutido.
- Detecta aspas ("") internas que podem confundir o processamento.
- Reporta linhas com problemas comuns de formatação.

Uso:
    python check_csv_issues.py --input caminho/arquivo.csv [--delimiter ';']

Saída:
    Relatório no terminal e arquivo "csv_issues_report.csv" com os problemas encontrados.
"""
import argparse
import csv
import sys
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="Verifica problemas comuns em arquivos CSV.")
    parser.add_argument('--input', required=True, help='Caminho do arquivo CSV a ser analisado.')
    parser.add_argument('--delimiter', default=';', help='Separador de colunas (padrão: ";").')
    return parser.parse_args()

def analyze_csv(input_path, delimiter):
    issues = []
    with open(input_path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar='"')
        try:
            header = next(reader)
        except Exception as e:
            print(f"Erro ao ler o cabeçalho: {e}")
            sys.exit(1)
        num_cols = len(header)
        for i, row in enumerate(reader, start=2):
            if len(row) != num_cols:
                issues.append({
                    'record_number': i,
                    'column_name': '',
                    'issue_type': 'col_count_mismatch',
                    'detail': f'Esperado {num_cols}, encontrado {len(row)}',
                    'sample': str(row)
                })
            for col_idx, value in enumerate(row):
                col_name = header[col_idx] if col_idx < len(header) else f'col_{col_idx+1}'
                if isinstance(value, str):
                    if delimiter in value:
                        issues.append({
                            'record_number': i,
                            'column_name': col_name,
                            'issue_type': 'embedded_delimiter',
                            'detail': f'Separador "{delimiter}" encontrado no campo',
                            'sample': value
                        })
                    if '"' in value:
                        issues.append({
                            'record_number': i,
                            'column_name': col_name,
                            'issue_type': 'internal_quote',
                            'detail': 'Aspas internas encontradas',
                            'sample': value
                        })
                    if value != value.strip():
                        issues.append({
                            'record_number': i,
                            'column_name': col_name,
                            'issue_type': 'leading_trailing_whitespace',
                            'detail': 'Espaços em branco no início/fim do campo',
                            'sample': value
                        })
    return header, issues

def write_report(header, issues):
    report_path = Path('csv_issues_report.csv')
    with report_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['record_number', 'column_name', 'issue_type', 'detail', 'sample'])
        for issue in issues:
            writer.writerow([
                issue['record_number'],
                issue['column_name'],
                issue['issue_type'],
                issue['detail'],
                issue['sample']
            ])
    print(f"Relatório salvo em {report_path.resolve()}")

def main():
    args = parse_args()
    header, issues = analyze_csv(args.input, args.delimiter)
    print(f"Total de problemas encontrados: {len(issues)}")
    for issue in issues:
        print(f"Linha {issue['record_number']} | Coluna: {issue['column_name']} | Tipo: {issue['issue_type']} | Detalhe: {issue['detail']} | Exemplo: {issue['sample']}")
    write_report(header, issues)

if __name__ == '__main__':
    main()
