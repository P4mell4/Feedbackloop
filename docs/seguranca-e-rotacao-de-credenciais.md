# Segurança e rotação de credenciais

1. Nunca adicionar chaves de API, senhas ou tokens ao código, README, issues ou capturas de tela.
2. Manter `.env` fora do Git; versionar somente `.env.example` com valores vazios/de exemplo.
3. Executar uma varredura de segredos antes de publicar e examinar o histórico Git.
4. Se uma credencial tiver sido exposta, revogá-la no provedor, emitir uma nova, atualizar o ambiente e verificar logs de uso.
5. Confirmar que a chave antiga deixou de funcionar; registrar data, responsável e resultado sem copiar o segredo para o documento.
6. Usar permissões mínimas e separar credenciais de desenvolvimento e produção.

## Evidência a anexar

- Comando e versão da ferramenta de varredura.
- Resultado resumido (sem reproduzir qualquer segredo).
- Registro de rotação, se aplicável.
- Confirmação de que `.env` não está versionado.

Não declarar varredura ou rotação concluída sem executar os passos no repositório real.
