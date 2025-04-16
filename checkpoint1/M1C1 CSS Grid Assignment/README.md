Preguntas teóricas:
# ¿Cuáles son algunas de las cosas que hacen que SCSS sea diferente de CSS? (coloca ejemplos).

SCSS agrega funcionalidades que simplifican y optimizan la escritura de CSS, ofreciendo características avanzadas no disponibles en CSS estándar. Permite definir variables reutilizables, anidar selectores css facilitando la oorganizacion y la legibilidad del código. Tambien permite definir bloques de código reutilizables llamados mixins, que pueden incluir propiedades CSS y variables algo que css no tiene.
```scss
$color-principal: #3498db;

nav {
  ul {
    li {
      a {
        color: $color-principal;
      }
    }
  }
}

@mixin borde-redondeado($radio) {
  border-radius: $radio;
  -webkit-border-radius: $radio;
  -moz-border-radius: $radio;
}

.boton {
  @include borde-redondeado(5px);
}
```


# ¿Qué es una variable SCSS? (porque crees que debes utilizarla pon un ejemplo de una variable, escribe una variable y como se pondría para utilizarla)

Una variable en SCSS es un contenedor reutilizable que almacena valores específicos (colores, tamaños, rutas, etc.) para su uso múltiple en hojas de estilo, se declara con $ y existe solo en tiempo de compilación. Son fundamentales para crear sistemas de diseño escalables y mantenibles. Su uso profesional ayuda a reducir errores, acelerar el desarrollo y permite crear arquitecturas CSS robustas. 
```scss
$tema-claro: (
  fondo: #ffffff,
  texto: #2c3e50,
  borde: #bdc3c7
);

.tema-claro {
  background-color: map-get($tema-claro, fondo);
  color: map-get($tema-claro, texto);
  border: 1px solid map-get($tema-claro, borde);
}

.boton {
  background-color: map-get($tema-claro, borde);
  color: map-get($tema-claro, texto);
  padding: 10px 20px;
  border-radius: 5px;
}
```

# ¿Qué es un SCSS Mixin? (porque crees que debes utilizarla pon un ejemplo de un mixin, escribiendo cómo se crea y como se pondría para utilizarla)

Un mixin es un bloque reutilizable de código SCSS que permite, encapsular declaraciones CSS complejas,recibir parámetros para personalizar su salida, evitar repetición de código mediante composición y tambien nos ayuda a incluir lógica condicional (@if, @for, @each).
```scss
@mixin sombra($nivel: 1, $color: rgba(0,0,0,0.1)) {
  @if $nivel == 1 {
    box-shadow: 0 1px 3px $color;
  } @else if $nivel == 2 {
    box-shadow: 0 3px 6px $color;
  } @else if $nivel == 3 {
    box-shadow: 0 10px 20px $color;
  } @else {
    @error "Nivel de sombra #{$nivel} no definido";
  }
}

.card {
  @include sombra(2);
}

.modal {
  @include sombra(3, rgba(0,0,0,0.2));
}
```

# ¿Qué significa Unidad fraccionaria (fr) con CSS Grid?
Es una unidad de medida flexible diseñada específicamente para distribuir el espacio disponible dentro de un contenedor de cuadrícula.