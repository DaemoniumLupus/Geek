

class Answer {  
    public static StringBuilder answer(String QUERY, String PARAMS){
        // Напишите свое решение ниже
        
        StringBuilder strBuild = new StringBuilder(QUERY);
        PARAMS = PARAMS.replaceAll("\\{|\\}", "");
        String[] paramStrings = PARAMS.split("\\,",0);

        System.out.println(paramStrings[0]);
        for (int i = 0; i < paramStrings.length;i++){
          String strKey = paramStrings[i].split(":")[0];
          strKey = strKey.replace("\"", "");
          strKey = strKey.replace(" ", "");
          
          String strValue = paramStrings[i].split(":")[1];
          strValue = strValue.replaceAll(" ", "");
          System.out.println(paramStrings[i]);
          if (strValue.equals("\"null\"")){
            continue;
          }
          if (i > 0){
            strBuild.append(" and ");
          }
          strBuild.append(strKey);
          strBuild.append("=");
          strBuild.append(strValue);
               
        }
        return strBuild;

    }
}


// Не удаляйте этот класс - он нужен для вывода результатов на экран и проверки
public class Printer{ 
	public static void main(String[] args) { 
      String QUERY = "";
      String PARAMS = "";
      
      if (args.length == 0) {
        // При отправке кода на Выполнение, вы можете варьировать эти параметры
        QUERY = "select * from students where ";
	    PARAMS = "{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"} ";
      }
      else{
        QUERY = args[0];
        PARAMS = args[1];
      }     
      
      Answer ans = new Answer();      
      System.out.println(ans.answer(QUERY, PARAMS));
	}
}