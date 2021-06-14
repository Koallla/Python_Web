PGDMP                         y           hw8    13.3    13.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16402    hw8    DATABASE     `   CREATE DATABASE hw8 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE hw8;
                postgres    false            �            1259    16416    Courses    TABLE     �   CREATE TABLE public."Courses" (
    id integer NOT NULL,
    course character varying NOT NULL,
    teatcher_id integer NOT NULL
);
    DROP TABLE public."Courses";
       public         heap    postgres    false            �            1259    16432    Grades    TABLE     �   CREATE TABLE public."Grades" (
    id integer NOT NULL,
    grade integer NOT NULL,
    course_id integer NOT NULL,
    teatcher_id integer NOT NULL,
    users_id integer NOT NULL,
    created_at timestamp without time zone
);
    DROP TABLE public."Grades";
       public         heap    postgres    false            �            1259    16408    Groups    TABLE     _   CREATE TABLE public."Groups" (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public."Groups";
       public         heap    postgres    false            �            1259    16403    Students    TABLE     �   CREATE TABLE public."Students" (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    surname character varying(30) NOT NULL,
    group_id integer NOT NULL
);
    DROP TABLE public."Students";
       public         heap    postgres    false            �            1259    16424 	   Teatchers    TABLE     b   CREATE TABLE public."Teatchers" (
    id integer NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public."Teatchers";
       public         heap    postgres    false            �          0    16416    Courses 
   TABLE DATA           <   COPY public."Courses" (id, course, teatcher_id) FROM stdin;
    public          postgres    false    202   �       �          0    16432    Grades 
   TABLE DATA           [   COPY public."Grades" (id, grade, course_id, teatcher_id, users_id, created_at) FROM stdin;
    public          postgres    false    204   4       �          0    16408    Groups 
   TABLE DATA           ,   COPY public."Groups" (id, name) FROM stdin;
    public          postgres    false    201   .       �          0    16403    Students 
   TABLE DATA           A   COPY public."Students" (id, name, surname, group_id) FROM stdin;
    public          postgres    false    200   c       �          0    16424 	   Teatchers 
   TABLE DATA           /   COPY public."Teatchers" (id, name) FROM stdin;
    public          postgres    false    203   �        8           2606    16423    Courses Courses_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public."Courses"
    ADD CONSTRAINT "Courses_pkey" PRIMARY KEY (id);
 B   ALTER TABLE ONLY public."Courses" DROP CONSTRAINT "Courses_pkey";
       public            postgres    false    202            <           2606    16436    Grades Grades_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT "Grades_pkey" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public."Grades" DROP CONSTRAINT "Grades_pkey";
       public            postgres    false    204            6           2606    16415    Groups Groups_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Groups"
    ADD CONSTRAINT "Groups_pkey" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public."Groups" DROP CONSTRAINT "Groups_pkey";
       public            postgres    false    201            4           2606    16407    Students Students_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT "Students_pkey" PRIMARY KEY (id);
 D   ALTER TABLE ONLY public."Students" DROP CONSTRAINT "Students_pkey";
       public            postgres    false    200            :           2606    16431    Teatchers Teatchers_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."Teatchers"
    ADD CONSTRAINT "Teatchers_pkey" PRIMARY KEY (id);
 F   ALTER TABLE ONLY public."Teatchers" DROP CONSTRAINT "Teatchers_pkey";
       public            postgres    false    203            >           2606    16442    Grades course_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT course_fk FOREIGN KEY (course_id) REFERENCES public."Courses"(id) NOT VALID;
 <   ALTER TABLE ONLY public."Grades" DROP CONSTRAINT course_fk;
       public          postgres    false    204    2872    202            =           2606    16437    Students group_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Students"
    ADD CONSTRAINT group_fk FOREIGN KEY (group_id) REFERENCES public."Groups"(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID;
 =   ALTER TABLE ONLY public."Students" DROP CONSTRAINT group_fk;
       public          postgres    false    200    2870    201            ?           2606    16447    Grades teatcher_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT teatcher_fk FOREIGN KEY (teatcher_id) REFERENCES public."Teatchers"(id) NOT VALID;
 >   ALTER TABLE ONLY public."Grades" DROP CONSTRAINT teatcher_fk;
       public          postgres    false    2874    203    204            @           2606    16452    Grades users_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public."Grades"
    ADD CONSTRAINT users_fk FOREIGN KEY (users_id) REFERENCES public."Students"(id) NOT VALID;
 ;   ALTER TABLE ONLY public."Grades" DROP CONSTRAINT users_fk;
       public          postgres    false    200    204    2868            �   O   x�3��M,�H�M,�L.�4�2�Ȩ,����9}2KR�KJ�R�\�TfN~q~AF%�!�)�KfAN~nbr%P_� ��t      �   �  x�}�[��8C��U�&p�ig-��u��Qt�^�?�2Y�l9�^���l���ڿ����M�[�s�c+�_��r�W��A�Uo�FP{���c�=����=����#�l+?��4�e��E-�� ��z�P1�djf��BAI� ����_"��P��R�[�,�p�M��	�P�yS(o�L�p(\H�.�Ѕ|�pI,&�o)��{��;���'�����,HOu@��@z���X�K�>�%�u�u��3U��.M;a�K�NӴ14�A�1a�P��U\�Ƙ��`�WZq��O�0�O� �擰6�[�It�|�1�|y5�3� �擰+��e���[��Z?�����4�3t9P�
ˇ.���'�R��D�jc�"���p~���p�}���p}��6��)��ٝ)ȩѝ)H�ɝ)h���LA,��LAM�D�PB�=S>ݢg�7}�^;���)̟��������������0��������:��&���w��J_��s�=u{[d��3����}�����:#�����Uz��]Y���~N�d3u��ZE%ʶK���$��$�9,��6"_8H"!_8�b�*�A	:s]$�����/�o�b�C'�_8�,�_8�,�_8�,�_�~��f�������	?s	~H��0W+־�~z�m�'�p1��U���q�cu\�X�X#%N0��D���c��Ǝ1Oba��=�s���>d����������ӱ`���9�-K�sFx��[Zxv҇�q��ߔǭ�epq�l��r��\Ơk��]�tmw�0����a�u}�a�u`Ӯ� q㮻 sw����N<�㮻 s�Cw����������0?t`~�.@\��מw���컵�Qω�O���F���Z���{�{�{>����V������M�p���؇����
',��;5%�SS�9GI�����JWnwnV�snV�sN��s���s�O�sjJ8���s���sΐ�s�TW�pnV�sk���I��t�G��X���՚b��Gw�:�4���6v q��>.A�`l���cǸ�a���lkNM1��M	�W{ZS�e��	�H�КbVhM1�p���{�)��_�`��q?����ZS�%�g�~X�aO�W�~\685��Кb~hM1�thM1��q�ũ)�i+ֿ���.'q�r��cpC�`���>�1x!V0+�	��x�!F0�`���5EX�ZS��5�|КbFhM1'������؋�-Ck�9�ZS�!ZS��wS���5Ŝ��+�����؏�mCk�9�n�9��5Ŝ_S���)���b�@��~T��fΪ[S���g;o��sk�1��sk�1��sk�1��sk�1��k~M�\�nMY�Z����qbnK1�cnG1�VcnC1�cn?1��a�m'��rb��&��jb�m&��bb��%��Zb�m%��R"���4c���HQI�MT�a����H�Oӷ��i;>-�ZF7�*z�ݝ�-�*z����~��y�      �   %   x�3��*���/�2���LI�I�2�,N���qqq ��	      �   H  x�=Q]o�0|������G`�cC*h�^\��i�Z�?���)���.�Aƹna�G������(��ZG=�4�agct�0N�x��[�	'����Y�w�P:YbG�+>ٷ,f�G{+qt��B0[
��ඉJI��?�"�ױ�kJks�*2��U�
�;�8�\�}oN��6%/*{k�e�8�<S;P�S٨�jhЪ��b��>����=5Xs��a�g:я�������ĉ:�A=����Rd.����:��B���>��r��_����	�T���ISe˰u���XS�*�eg�����X��s���)I�?Q��E      �   *   x�3��,K��/�2�H-)2�9}K3sSS�2�1z\\\ ��     