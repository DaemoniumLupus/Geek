package Lesson3;

import java.time.DateTimeException;
import java.util.regex.Pattern;
import java.util.zip.DataFormatException;

public class Parse {
    private String[] strArray;
    private String first;
    private String second;
    private String third;
    private String bithDay;
    private long phoneNumber;
    private char sex;
    private int count;

    public Parse(String str) throws Exception{
        count = 6;
        strArray = str.split(" ");
        Pattern phonePattern = Pattern.compile("\\d{11}");
        Pattern FIOPattern = Pattern.compile("[A-ZА-Я]{1}[a-zа-я]+");
        Pattern bithPattern = Pattern.compile("\\d{2}[.]\\d{2}[.]\\d{4}");

        //Проверка количества данных
        if (strArray.length < 6){
            throw new DataFormatException("Данных недостаточно!");
        }else if (strArray.length > 6) {
            throw new DataFormatException("Данных слишком много!");
        }
        for (String data : strArray){
            if (phonePattern.matcher(data).find()){
                phoneNumber = Long.parseLong(data);
                count -= 1;
            }else if (bithPattern.matcher(data).find()){
                bithDay = data;
                count -= 1;
            }else if(data.length() == 1 && (data.equals("f") || data.equals("m"))){
                sex = data.charAt(0);
                count -= 1;
            }else if (FIOPattern.matcher(data).find()){
                if(first == null){
                    first = data;
                }else if(second == null){
                    second = data;
                }else if (third == null){
                    third = data;
                }
                count -= 1;
            }
        }
        if (count != 0){
            if (phoneNumber == 0){
                throw new NumberFormatException("Non correct phone number!");
            }else if (bithDay == null){
                throw new DateTimeException("Non correct bith day!");
            }else if (sex != 'f' || sex != 'm'){
                throw new Exception("Non correct sex!");
            }else if(first == null || second == null || third == null){
                throw new Exception("Non correct FIO!");
            }
        }
    }

    public String getFirst(){
        return first;
    }

    public String getDataString(){
        return first + " " + second + " " + third + ' ' + bithDay + ' ' + phoneNumber + ' ' + sex;
    }
}
