from .build.build_produtos import BuildProdutos


def create_payload_produto():
    """
        Cria o payload padrão para geração de produto.
        \n
        Returns
        -------
        Payload de usuário preenchido com informações básicas geradas aleatóriamente.
    """
    return BuildProdutos.build_payload()
