package Enumerados;

import java.time.LocalDate;
import java.util.Scanner;

import Enumerados.model.Genero;
import Enumerados.model.Persona;

public class Principal {

	public static void main(String[] args) {
		
		LocalDate actual = LocalDate.now();
		Persona p = new Persona("Pedro", "Sánchez", Genero.HOMBRE, actual);
		
		LocalDate unDia = LocalDate.of(2020, 3, 3);
		
		Genero generoIntroducido = null;
		do {
			try {
				System.out.println("Introduzca el género: ");
				String generoComoString = new Scanner(System.in).nextLine();
				generoIntroducido = Genero.valueOf(generoComoString.toUpperCase());
			} catch (Exception exception) {
				System.out.println("El valor introducido no es correcto (Hombre/Mujer): ");
			}
		} while (generoIntroducido==null);
		
		Persona p_2 = new Persona ("Antonio", "Sánchez", generoIntroducido, unDia);
		
		System.out.println(p_2);
		
		Persona [] grupo = new Persona[6];
		
		Persona Antonio = new Persona ("Antonio", "Sánchez", generoIntroducido, unDia);
		Persona Pedro = new Persona ("Pedro", "Benítez", generoIntroducido, unDia);
		Persona Alfonso = new Persona ("Alfonso", "Salado", generoIntroducido, unDia);
		
		grupo[0] = Antonio;
		grupo[1] = Pedro;
		grupo[2] = Alfonso;
		grupo[3] = new Persona ("Manuela", "Sánchez", generoIntroducido, unDia);
		grupo[4] = new Persona ("Alejandra", "Sánchez", generoIntroducido, unDia);
		grupo[5] = new Persona ("Eustaquio", "Sánchez", generoIntroducido, unDia);
		
	}

}
