package SieteYMedia.model;

public class Carta {
	private Palo palo;
	private int numero;
	
	public Carta(int numero, Palo palo) throws Exception {
		super();
		if (numero < 1 || numero > 12 || numero == 8 || numero == 9) {
			throw new Exception("Valor no válido, debe ser un valor entre 1 y 7 o entre 10 y 12.");
		}
		this.palo = palo;
		this.numero = numero;
	}
	
	public double getValor() {
		return this.numero > 9 ? 0.5 : this.numero;
	}
	
	public String toString() {
		return String.format("%s de %s", this.numero, this.palo.toString().toLowerCase());
	}
	
	public int compareTo(Carta o) {
		return this.numero - o.numero;
	}
	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = this == obj;
		
		if (!sonIguales && obj != null && obj instanceof Carta) {
			Carta casteado = (Carta)obj;
			
			sonIguales = casteado.numero == this.numero
					&& casteado.palo == this.palo;
		}
		
		return sonIguales;
	}
	
}
