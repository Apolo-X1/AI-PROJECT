public class CLIMATE {

    public static void main(String[] args) {
        String weather = "sunny";
//Nos muestra un mensaje dependiendo el clima actual
        switch (weather){
            case "sunny":
                System.out.println("El tiempo es soleado");
                break;
            case "cloudy":
                System.out.println("El tiempo esta soleado");
                break;
            default:
                System.out.println("No se ha podido identificar el clima");
        }
    }
}