public class CLIMATE {

    public static void main(String[] args) {
        String weather = "snowfall";
//Nos muestra un mensaje dependiendo el clima actual
//Agregamos mas tipos de climas y advertencias
        switch (weather){
            case "sunny":
                System.out.println("El tiempo es soleado.");
                break;
            case "cloudy":
                System.out.println("El tiempo esta soleado.");
                break;
            case "rain":
                System.out.println("El dia es lluvioso.");
                break;
            case "hurricane":
                System.out.println("¡Mantengase en un lugar seguro, huracan!"); 
                break;
            case "snowfall":
                System.out.println("¡Esta nevando, guarde resguardo en casa!");
                break;
            default:
                System.out.println("No se ha podido identificar el clima.");
        }
    }
}