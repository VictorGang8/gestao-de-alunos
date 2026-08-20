import streamlit as st

from banco import (
    criar_tabela,
    cadastrar_aluno,
    excluir_aluno,
    listar_alunos,
    quantidade_alunos,
)


st.set_page_config(page_title='Gestão de Alunos', page_icon='🎓', layout='wide')
criar_tabela()

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #eef4ff 0%, #f8fafc 100%);
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        div[data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('🎓 Cadastro de alunos')
st.caption('Gerencie os alunos de forma simples e visualmente organizada.')

col_form, col_metric = st.columns([1.6, 1])

with col_form:
    with st.form('cadastro_aluno', clear_on_submit=True):
        st.subheader('Adicionar novo aluno')
        nome = st.text_input('Nome do aluno', placeholder='Ex.: Ana Souza')
        idade = st.number_input('Idade', min_value=0, max_value=120, value=18)
        curso = st.text_input('Curso', placeholder='Ex.: Engenharia')

        enviado = st.form_submit_button('Cadastrar aluno', use_container_width=True)

        if enviado:
            if not nome.strip() or not curso.strip():
                st.warning('Preencha nome e curso antes de cadastrar.')
            else:
                cadastrar_aluno(nome, idade, curso)
                st.success('Aluno cadastrado com sucesso!')
                st.rerun()

with col_metric:
    total_alunos = quantidade_alunos()
    st.metric('Total de alunos', total_alunos)
    if total_alunos:
        idade_media = round(
            sum(aluno[2] for aluno in listar_alunos() if aluno[2] is not None) / total_alunos,
            1,
        )
        st.metric('Média de idade', idade_media)
    else:
        st.metric('Média de idade', 0)

st.subheader('Lista de alunos')

alunos = listar_alunos()

if not alunos:
    st.info('Nenhum aluno cadastrado ainda.')
else:
    for aluno in alunos:
        aluno_id, nome, idade, curso = aluno
        col_id, col_nome, col_idade, col_curso, col_acao = st.columns([0.7, 2.2, 1.2, 2.6, 1.2])

        with col_id:
            st.write(f'#{aluno_id}')
        with col_nome:
            st.write(nome)
        with col_idade:
            st.write(f'{idade} anos')
        with col_curso:
            st.write(curso)
        with col_acao:
            if st.button('Excluir', key=f'delete_{aluno_id}', use_container_width=True):
                excluir_aluno(aluno_id)
                st.success(f'Aluno #{aluno_id} removido com sucesso!')
                st.rerun()

        st.divider()

