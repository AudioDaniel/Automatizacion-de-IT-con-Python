#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import reportlab
import datetime


def generate_report(ruta):
    report = SimpleDocTemplate(ruta)
    styles = getSampleStyleSheet()
    report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])


if __name__ == "__main__":
    pass
