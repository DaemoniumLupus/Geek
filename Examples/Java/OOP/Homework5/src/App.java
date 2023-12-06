package Homework5.src;

import java.util.Map;
import java.util.NoSuchElementException;

public class App {
    public static void main(String[] args) throws Exception {
        new ReportService(Map.of(
            "pdf", new PDF_1(),
            "xml", new XML(),
            "json", new JSON()
        ));
        /**
         * Класс документ - описывает структуру документа.
         *
         * Нужно спроектировать систему отчетов, которая будет формировать отчеты для документа.
         *
         * 1. Формирование PDF-файла (потенциально может быть несколько типом разметки PDF-файла).
         * 2. Формирование JSON-файла с полями документа.
         * 3. Формирование XML-файла с полями документа.
         * 4. ... потенциально могут добавляться разные типы отчетов.
         *
         * После реализации задать себе 2 вопроса и прикрепить их к сданной ДЗ:
         * 1. Насколько сложно добавить поддержку нового типа отчета?
         * 2. Как будет выглядеть проект, если в нем будет 1000+ типов отчетов?
         *
         *
         */
    }
    

    static class ReportService {
        private Map<String,Report> reportsMap;
        
        public ReportService(Map<String,Report> reportsMap){
            this.reportsMap = reportsMap;
        }
        
        public byte[] createReport(Document document, String reportType) {
        // reportType = {"pdf-1", "json", "xml", ...}

        Report report = reportsMap.get(reportType);

        if(report == null){
            throw new NoSuchElementException("No report with this type: \"" + reportType + "\"");
        }

        
        return report.createReport(document);
        }

    }

    static class Document {
        private long id;
        private String number;
        // ...
    }

    

    static class PDF_1  implements Report{
        @Override
        public byte[] createReport(Document document){
            byte[] data = null;
            //Code for create orders
            return data;
        }
    }

    static class XML implements Report{
        @Override
        public byte[] createReport(Document document){
            byte[] data = null;
            //Code for create orders
            return data;
        }
    }

    
    static class JSON implements Report{
        @Override
        public byte[] createReport(Document document){
            byte[] data = null;
            //Code for create orders
            return data;
        }
    }

    

    
    public interface Report{
        byte[] createReport(Document document);
        
    }

    
}