import shutil
import os
from pathlib import Path

post_path = 'D:\OneDrive - zju.edu.cn\桌面\codes\cuixiaodao.github.io\_posts\2021-09-14-k8s-applications.md'


def sync_post(post_fn:str):
    src_path = Path('posts', post_fn)
    file_stem = src_path.stem
    # file_ext = src_path.suffix
    
    dst_path = Path('_posts', post_fn)
    Path.cwd
    # copy post from src to dst
    shutil.copyfile(src_path.absolute(), dst_path.absolute())

    # update img path
    dst_path.write_text(dst_path.read_text(encoding='utf-8').replace('(assets/', '(/assets/images/'), encoding='utf-8')

    # copy post images from src to dst
    asset_src_dir = Path('posts/assets', file_stem)
    asset_dst_dir = Path('assets/images', file_stem)
    shutil.copytree(asset_src_dir.absolute(), asset_dst_dir.absolute(), dirs_exist_ok=True)
    print('sync finished')

def main():
    sync_post('2021-09-14-k8s-applications.md')

if __name__ == '__main__':
    main()