# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py', 'word_cloud.py', 'shixi.py', 'scale.py', 'positiontype_salarymean_and_number.py', 'position_type.py', 'hotcompany_position.py', 'finance_salary.py', 'finance.py', 'experience_salary.py', 'experience_command.py', 'degree_salary.py', 'degree_command.py', 'data_preprocess.py', 'data_from_mysql.py', 'data_after_process.py', 'company_type.py', 'company_scale_salary.py', 'cityposition_number.py', 'city_salary.py', 'city_condition.py'],
             pathex=['C:\\Users\\79000\\Desktop\\ʵѵ\\���ݿ��ӻ�'],
             binaries=[],
             datas=[],
             hiddenimports=['jupyter_echarts_pypkg','pyecharts_snapshot','tornado','pyecharts_snapshot.environment','echarts-countries-pypkg','echarts-china-provinces-pypkg','echarts-china-cities-pypkg','echarts-countries-pypkg','echarts-china-provinces-pypkg','echarts-china-cities-pypkg'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
