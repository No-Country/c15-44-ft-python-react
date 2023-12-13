window.addEventListener("load", () => {
  const form = document.querySelector("#formulario");
  const email = document.getElementById("correo");
  const pass = document.getElementById("password");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    validaCampos();
  });

  const validaCampos = () => {
    const emailValor = email.value.trim();
    const passValor = pass.value.trim();

    //validando campo email
    if (!emailValor) {
      validaFalla(email, "Campo vacío");
    } else if (!validaEmail(emailValor)) {
      validaFalla(email, "El e-mail no es válido");
    } else {
      validaOk(email, "👍🏻");
      emailValido = true;
    }
    //validando campo password
    const er =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#.$($)$-$_])[A-Za-z\d$@$!%*?&#.$($)$-$_]{8,16}$/;
    if (!passValor) {
      validaFalla(pass, "Campo vacío");
    } else if (passValor.length < 8) {
      validaFalla(pass, "Debe tener 8 caracteres cómo mínimo.");
    } else if (!passValor.match(er)) {
      validaFalla(
        pass,
        "Debe tener al menos una may., una min., un símbolo. y un núm."
      );
    } else {
      validaOk(pass, "👍🏻");
      passValido = true;
    }
    // Acceder a trabajos
    if (emailValido && passValido) {
      setTimeout(() => {
        window.location.href = "../pages/trabajo.html";
      }, 3000);
    }
  };

  const validaFalla = (input, msje) => {
    const formControl = input.parentElement;
    const aviso = formControl.querySelector("p");
    aviso.innerText = msje;
    formControl.className = "form-control falla";
  };
  const validaOk = (input, msje) => {
    const formControl = input.parentElement;
    const aviso = formControl.querySelector("p");
    aviso.innerText = msje;
    formControl.className = "form-control ok";
  };

  const validaEmail = (email) => {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
      email
    );
  };
});

let x = document.getElementById("password");
function myFunctionLogin() {
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
