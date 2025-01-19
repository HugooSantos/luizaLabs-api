"""Create products table

Revision ID: 2d9fafdc6a23
Revises: 
Create Date: 2025-01-18 14:47:54.334611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker	


# revision identifiers, used by Alembic.
revision: str = '2d9fafdc6a23'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('path_image', sa.String(), nullable=False),
    sa.Column('ean', sa.String(length=13), unique=True, nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('sales_location', sa.String(length=10), nullable=False),
    sa.Column('active', sa.Boolean(), default=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=False), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=False), server_default=sa.text('now()'), onupdate=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    products = """
    INSERT INTO products (name, path_image, ean, price, description, sales_location, active)
    VALUES
    ('Apple iPhone 14', 'static/image/iphone-14.jpeg', '1901984321098', 699.99, 'Smartphone com tela OLED de 6,1 polegadas, câmera de 12 MP e chip A15 Bionic.', 'event', true),
    ('Samsung Galaxy S22', 'static/image/Samsung-Galaxy-S22.jpeg', '1901984321105', 799.99, 'Smartphone com tela Dynamic AMOLED de 6,1 polegadas, câmera de 50 MP e chip Exynos 2200.', 'event', true),
    ('Sony PlayStation 5', 'static/image/PlayStation-5.jpeg', '1901984321112', 499.99, 'Console de videogame com suporte a 4K, memória SSD e controle DualSense.', 'store', true),
    ('Dell XPS 13', 'static/image/Dell-XPS-13.jpeg', '1901984321129', 999.99, 'Notebook ultrafino com tela de 13 polegadas, processador Intel i7 e 16 GB de RAM.', 'event', true),
    ('Samsung 55" 4K UHD TV', 'static/image/Samsung-55-4K-UHD.jpeg', '1901984321136', 649.99, 'TV de 55 polegadas com resolução 4K UHD, HDR10+ e som Dolby Atmos.', 'store', true),
    ('Bose QuietComfort 35 II', 'static/image/Bose-QuietComfort.jpeg', '1901984321143', 299.99, 'Fones de ouvido com cancelamento de ruído, conectividade Bluetooth e som de alta qualidade.', 'event', true),
    ('Nike Air Max 270', 'static/image/Nike-Air-Max.jpeg', '1901984321150', 149.99, 'Tênis esportivo com tecnologia Air Max, design moderno e conforto extremo.', 'store', true),
    ('Apple AirPods Pro 2', 'static/image/Apple-AirPods.jpg', '1901984321167', 249.99, 'Fones de ouvido sem fio com cancelamento ativo de ruído e áudio espacial.', 'event', true),
    ('Samsung Galaxy Watch 5', 'static/image/Samsung-Galaxy.jpeg', '1901984321174', 249.99, 'Smartwatch com monitoramento de saúde, GPS integrado e resistência à água.', 'store', true),
    ('Microsoft Surface Pro 8', 'static/image/Microsoft-Surface.jpeg', '1901984321181', 1099.99, 'Tablet 2 em 1 com tela de 13 polegadas, processador Intel i7 e 16 GB de RAM.', 'event', true),
    ('Fitbit Charge 5', 'static/image/Fitbit-Charge.jpeg', '1901984321198', 179.99, 'Pulseira fitness com monitoramento de batimentos cardíacos, sono e atividades físicas.', 'store', true),
    ('GoPro HERO10 Black', 'static/image/GoPro-HERO.jpeg', '1901984321204', 399.99, 'Câmera de ação com gravação em 5K, resistência à água e estabilidade de imagem avançada.', 'event', true),
    ('LG 65" OLED TV', 'static/image/LG-65-OLED.jpeg', '1901984321211', 1799.99, 'TV OLED de 65 polegadas com qualidade de imagem superior, som Dolby Atmos e design fino.', 'store', true),
    ('Canon EOS Rebel T7', 'static/image/Canon-EOS-Rebel-T7.jpeg', '1901984321228', 499.99, 'Câmera DSLR com lente de 18-55mm, sensor de 24.1 MP e gravação em Full HD.', 'event', true),
    ('Fitbit Versa 3', 'static/image/Fitbit-Versa-3.jpeg', '1901984321235', 229.99, 'Smartwatch fitness com monitoramento de saúde, GPS e autonomia de até 6 dias.', 'store', true),
    ('Razer DeathAdder V2', 'static/image/Razer-DeathAdder-V2.jpeg', '1901984321242', 69.99, 'Mouse gamer ergonômico com sensor óptico de 20.000 DPI e iluminação RGB personalizável.', 'event', true),
    ('Asus ROG Strix G15', 'static/image/Asus-ROG-Strix-G15.jpeg', '1901984321259', 1399.99, 'Notebook gamer com tela de 15,6 polegadas, processador Ryzen 7 e GPU GeForce RTX 3060.', 'store', true),
    ('iRobot Roomba 692', 'static/image/iRobot-Roomba-692.jpeg', '1901984321266', 299.99, 'Robô aspirador com conectividade Wi-Fi, limpeza programada e detecção de sujeira.', 'event', true),
    ('Xiaomi Mi Band 6', 'static/image/Xiaomi-Mi-Band-6.jpeg', '1901984321273', 44.99, 'Pulseira fitness com monitoramento de atividades, sono e oxigenação do sangue.', 'store', true),
    ('Oculus Quest 2', 'static/image/Oculus-Quest-2.jpeg', '1901984321280', 299.99, 'Óculos de realidade virtual autônomos, com display de 1832x1920 por olho e controle sem fio.', 'event', true),
    ('Apple MacBook Air M1', 'static/image/Apple-MacBook-Air-M1.jpeg', '1901984321297', 999.99, 'Notebook ultrafino com chip M1, 8 GB de RAM e 256 GB de armazenamento SSD.', 'event', true),
    ('Sony WH-1000XM4', 'static/image/Sony-WH-1000XM4.jpeg', '1901984321303', 348.00, 'Fones de ouvido sem fio com cancelamento de ruído e até 30 horas de autonomia.', 'store', true),
    ('Nintendo Switch', 'static/image/Nintendo-Switch.jpeg', '1901984321310', 299.99, 'Console híbrido com tela de 6,2 polegadas, suportando jogos tanto em modo portátil quanto na TV.', 'event', true),
    ('Philips Sonicare ProtectiveClean 6100', 'static/image/Philips-Sonicare-ProtectiveClean-6100.jpeg', '1901984321327', 79.99, 'Escova de dentes elétrica com tecnologia de pressão ideal e 3 modos de limpeza.', 'store', true),
    ('Samsung Galaxy Tab S7', 'static/image/Samsung-Galaxy-Tab-S7.jpeg', '1901984321334', 649.99, 'Tablet Android com tela de 11 polegadas, processador Snapdragon e suporte a S Pen.', 'event', true),
    ('JBL Flip 5', 'static/image/JBL-Flip-5.jpeg', '1901984321341', 119.99, 'Caixa de som Bluetooth com som potente, resistente à água e até 12 horas de reprodução.', 'store', true),
    ('Anker PowerCore 10000', 'static/image/Anker-PowerCore-10000.jpeg', '1901984321358', 25.99, 'Carregador portátil compacto com capacidade de 10000mAh e tecnologia de carregamento rápido.', 'event', true),
    ('LG UltraGear 27GN950-B', 'static/image/LG-UltraGear-27GN950-B.jpg', '1901984321365', 599.99, 'Monitor gamer de 27 polegadas com resolução 4K, taxa de atualização de 144Hz e tempo de resposta de 1ms.', 'store', true),
    ('Sennheiser Momentum 3', 'static/image/Sennheiser-Momentum-3.jpeg', '1901984321372', 399.99, 'Fones de ouvido com cancelamento de ruído, som de alta definição e conectividade sem fio.', 'event', true),
    ('Acer Predator Helios 300', 'static/image/Acer-Predator-Helios-300.jpeg', '1901984321389', 1499.99, 'Notebook gamer com tela de 15,6 polegadas, processador Intel i7 e GPU NVIDIA GeForce RTX 3070.', 'store', true),
    ('Logitech G Pro X', 'static/image/Logitech-G-Pro-X.jpeg', '1901984321396', 129.99, 'Headset gamer com microfone Blue VO!CE, som DTS Headphone:X 2.0 e design leve.', 'event', true),
    ('Garmin Forerunner 945', 'static/image/Garmin-Forerunner-945.jpeg', '1901984321402', 499.99, 'Relógio GPS para atletas com monitoramento avançado de saúde e treinamento.', 'store', true)
    """

    Session = sessionmaker(bind=op.get_bind())
    session = Session()
    session.execute(sa.text(products))
    session.commit()


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
