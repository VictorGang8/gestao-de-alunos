const alunos = [
  { id: 1, nome: 'João Silva', idade: 20, curso: 'Engenharia' },
  { id: 2, nome: 'Maria Souza', idade: 22, curso: 'Direito' },
  { id: 3, nome: 'Pedro Costa', idade: 19, curso: 'Administração' }
];

const formAluno = document.getElementById('formAluno');
const listaAlunos = document.getElementById('listaAlunos');
const status = document.getElementById('status');
const totalAlunos = document.getElementById('totalAlunos');
const mediaIdade = document.getElementById('mediaIdade');
const totalCursos = document.getElementById('totalCursos');

function mostrarStatus(mensagem, tipo = 'sucesso') {
  status.textContent = mensagem;
  status.className = `status ${tipo === 'sucesso' ? 'status-success' : 'status-error'}`;
}

function renderTabela() {
  if (!alunos.length) {
    listaAlunos.innerHTML = '<tr><td colspan="5">Nenhum aluno cadastrado.</td></tr>';
  } else {
    listaAlunos.innerHTML = alunos
      .map(
        (aluno) => `
          <tr>
            <td>${aluno.id}</td>
            <td>${aluno.nome}</td>
            <td>${aluno.idade}</td>
            <td>${aluno.curso}</td>
            <td><button class="action-btn" data-id="${aluno.id}">Excluir</button></td>
          </tr>
        `
      )
      .join('');
  }

  const total = alunos.length;
  totalAlunos.textContent = total;

  if (total > 0) {
    const idadeMedia = alunos.reduce((soma, aluno) => soma + Number(aluno.idade || 0), 0) / total;
    mediaIdade.textContent = idadeMedia.toFixed(1);
    totalCursos.textContent = new Set(alunos.map((aluno) => aluno.curso.trim())).size;
  } else {
    mediaIdade.textContent = '0';
    totalCursos.textContent = '0';
  }
}

formAluno.addEventListener('submit', (event) => {
  event.preventDefault();

  const nome = document.getElementById('nome').value.trim();
  const idade = Number(document.getElementById('idade').value);
  const curso = document.getElementById('curso').value.trim();

  if (!nome || !curso || Number.isNaN(idade)) {
    mostrarStatus('Preencha todos os campos antes de salvar.', 'erro');
    return;
  }

  const novoAluno = {
    id: alunos.length ? alunos[alunos.length - 1].id + 1 : 1,
    nome,
    idade,
    curso
  };

  alunos.push(novoAluno);
  renderTabela();
  formAluno.reset();
  mostrarStatus('Aluno cadastrado com sucesso!');
});

document.addEventListener('click', (event) => {
  const botao = event.target.closest('.action-btn');
  if (!botao) {
    return;
  }

  const alunoId = Number(botao.dataset.id);
  const index = alunos.findIndex((aluno) => aluno.id === alunoId);

  if (index !== -1) {
    const alunoRemovido = alunos[index].nome;
    alunos.splice(index, 1);
    renderTabela();
    mostrarStatus(`${alunoRemovido} foi removido com sucesso.`);
  }
});

renderTabela();
