const conteudo = document.getElementById('conteudo');
conteudo.innerHTML = 'Novo conteúdo do elemento div.';

const elementosP = document.getElementsByTagName('p');
      for(let i = 0; i < elementosP.length; i++){
        elementosP[i].style.fontWeight = 'bold';
      }